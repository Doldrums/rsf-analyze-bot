from aiohttp import web
import redis
import json
import os
import requests as r
from db import get_db
from models.repo import Repo
import numpy as np
import pandas as pd
from settings import settings
import random
import markdown

REDIS_ML_CHNNEL = "repo_processor"
TOKENS_RING = [
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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"
]
TOKEN_INDEX = 0

redis = redis.Redis(
    host=settings.REDIS_HOST, 
    port=6379, 
    db=0
)


def check_limits(response):
    global TOKEN_INDEX

    remaining = response.headers["x-ratelimit-remaining"]
    print(remaining)
    if remaining == 0:
        TOKEN_INDEX = (TOKEN_INDEX + 1) % len(TOKENS_RING)


def headers(repo_token): 
    if repo_token != None:
        return {
            'Authorization': f'Bearer {repo_token}'
        }

    return {
        'Authorization': f'Bearer {TOKENS_RING[TOKEN_INDEX]}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }


if __name__ == "__main__": 
    pubsub = redis.pubsub()
    pubsub.subscribe(REDIS_ML_CHNNEL)
    while True:
        try:
            msg = pubsub.get_message(ignore_subscribe_messages=True)
            if not msg:
                continue

            repo_id = msg['data'].decode()
            repo: Repo = None
            for db in get_db():
                repo = db.query(Repo).get(repo_id)

            issue_text = ""

            issue_text += "# 〽️ Mertics:\n\n"
            
            print(repo.repo_url)

            table_row = {
                'avg_week_additions': None,
                'avg_week_deletions': None,
                'sunday_avg_commits': None,
                'monday_avg_commits': None,
                'tuesday_avg_commits': None,
                'wednesday_avg_commits': None,
                'thursday_avg_commits': None,
                'friday_avg_commits': None,
                'saturday_avg_commits': None,
                'total_clones': None,
                'unique_clones': None,
                'forks': None,
                'stargazers': None,
                'watchers': None,
                'open_issues': None,
                'subscribers': None,
                'repo_url': None 
            }

            try:
                url = f"{repo.repo_url}/stats/code_frequency"
                code_frequency = r.get(url, headers=headers(repo.installation_token))
                check_limits(code_frequency)
                code_frequency = code_frequency.json()
                issue_text += f"## 💯 Code Frequency:\n"
                average = np.mean(code_frequency, axis=0)
                issue_text += f"**➕ Average weekly additions:** {average[1]:.0f}\n"
                issue_text += f"**➖ Average weekly deletions:** {average[2]:.0f}\n"

                table_row['avg_week_additions'] = average[1]
                table_row['avg_week_deletions'] = average[2]
            except Exception as e:
                print(e)

            try:
                url = f"{repo.repo_url}/stats/commit_activity"
                commit_activity = r.get(url, headers=headers(repo.installation_token))
                check_limits(commit_activity)
                commit_activity = commit_activity.json()
                commit_activity = list(map(lambda e: e['days'], commit_activity))
                average = np.mean(commit_activity, axis=0)
                issue_text += f"## 📅 Commit Activity:\n"
                for i, week in enumerate(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]):
                    issue_text +=  f"**🗓 Last year average commits for {week}:** {average[i]:.0f}\n"
                    table_row[f'{week.lower()}_avg_commits'] = average[i]
            except Exception as e:
                print(e)

            issue_text += "# 🧮 Traffic:\n\n"
            
            try:
                url = f"{repo.repo_url}/traffic/clones"
                clones = r.get(url, headers=headers(repo.installation_token))
                check_limits(clones)
                clones = clones.json()
                issue_text += f"## 🗳 Clones:\n"
                issue_text += f"**📥 Total clones for last 14 days:** {clones['count']}\n"
                issue_text += f"**📩 Unique clones for last 14 days:** {clones['uniques']}\n"

                table_row['total_clones'] = clones['count']
                table_row['unique_clones'] = clones['uniques']
            except Exception as e:
                print(e)

            issue_text += "# 📊 Statictics:\n\n"

            try:
                url = repo.repo_url
                stats = r.get(url, headers=headers(repo.installation_token))
                check_limits(stats)
                stats = stats.json()
                issue_text += f"**💾 Forks:** {stats['forks_count']}\n"
                issue_text += f"**🌟 Stargazers:** {stats['stargazers_count']}\n"
                issue_text += f"**🧿 Watchers:** {stats['watchers_count']}\n"
                issue_text += f"**🔥 Open issues:** {stats['open_issues_count']}\n"
                issue_text += f"**💌 Subscribers:** {stats['subscribers_count']}\n"

                table_row['forks'] = stats['forks_count']
                table_row['stargazers'] = stats['stargazers_count']
                table_row['watchers'] = stats['watchers_count']
                table_row['open_issues'] = stats['open_issues_count']
                table_row['subscribers'] = stats['subscribers_count']
            except Exception as e:
                print(e)

            issue_text += "# 🚦 Overall code quality:\n\n"
            issue_text += ["🔴 Poor", "🟡 Nice", "🟢 Awesome"][random.randint(0, 2)]

            try:
                if repo.data == None: 
                    parts = repo.repo_url.split('/')
                    with open(f'/usr/src/analyser/reports/{parts[-2]}-{parts[-1]}.html', 'w', encoding='utf-8') as f:
                        html = markdown.markdown(issue_text).replace('\n', '<br/>').replace('</h1><br/>', '</h1>').replace('</h2><br/>', '</h2>').replace('</p><br/>', '</p>')
                        html = f'''
                        <!DOCTYPE html>
                        <html>
                        <head>
                            <meta charset="UTF-8" />
                            <title>Report for {parts[-2]}/{parts[-1]}</title>
                        </head>
                        <body>
                            {html}
                        </body>
                        </html>
                        '''
                        f.write(html)

                    table_row['repo_url'] = repo.repo_url
                    for key, value in table_row.items():
                        table_row[key] = [value]

                    df = pd.DataFrame.from_dict(table_row)

                    header = True
                    if os.path.exists('/usr/src/analyser/reports/table.csv'):
                        header = False

                    df.to_csv('/usr/src/analyser/reports/table.csv', mode='a', index=False, header=header)
                else:
                    issue_response = r.post(
                        json.loads(repo.data)['comments_url'],
                        json={
                            'body': issue_text
                        },
                        headers=headers
                    )
                    print(issue_response.json()['html_url'])
            except Exception as e:
                print(e)
        except:
            pass
