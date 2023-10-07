from aiohttp import web
import redis
import json
import requests as r
from db import get_db
from models.repo import Repo
import numpy as np
from settings import settings
import random
import markdown

REDIS_ML_CHNNEL = "repo_processor"

redis = redis.Redis(
    host=settings.REDIS_HOST, 
    port=6379, 
    db=0
)

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
            headers = {}
            if repo.installation_token != None:
                headers = {
                    'Authorization': f'Bearer {repo.installation_token}'
                }
            else:
                headers = {
                    # 'Authorization': f'Bearer {repo.installation_token}'
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
                }

            try:
                url = f"{repo.repo_url}/stats/code_frequency"
                code_frequency = r.get(url, headers=headers)
                code_frequency = code_frequency.json()
                issue_text += f"## 💯 Code Frequency:\n"
                average = np.mean(code_frequency, axis=0)
                issue_text += f"**➕ Average weekly additions:** {average[1]:.0f}\n"
                issue_text += f"**➖ Average weekly deletions:** {average[2]:.0f}\n"
            except Exception as e:
                print(e)

            try:
                url = f"{repo.repo_url}/stats/commit_activity"
                commit_activity = r.get(url, headers=headers)
                commit_activity = commit_activity.json()
                commit_activity = list(map(lambda e: e['days'], commit_activity))
                average = np.mean(commit_activity, axis=0)
                issue_text += f"## 📅 Commit Activity:\n"
                for i, week in enumerate(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]):
                    issue_text +=  f"**🗓 Last year average commits for {week}:** {average[i]:.0f}\n"
            except Exception as e:
                print(e)

            issue_text += "# 🧮 Traffic:\n\n"
            
            try:
                url = f"{repo.repo_url}/traffic/clones"
                clones = r.get(url, headers=headers)
                clones = clones.json()
                issue_text += f"## 🗳 Clones:\n"
                issue_text += f"**📥 Total clones for last 14 days:** {clones['count']}\n"
                issue_text += f"**📩 Unique clones for last 14 days:** {clones['uniques']}\n"
            except Exception as e:
                print(e)

            issue_text += "# 📊 Statictics:\n\n"

            try:
                url = repo.repo_url
                stats = r.get(url, headers=headers)
                stats = stats.json()
                issue_text += f"**💾 Forks:** {stats['forks_count']}\n"
                issue_text += f"**🌟 Stargazers:** {stats['stargazers_count']}\n"
                issue_text += f"**🧿 Watchers:** {stats['watchers_count']}\n"
                issue_text += f"**🔥 Open issues:** {stats['open_issues_count']}\n"
                issue_text += f"**💌 Subscribers:** {stats['subscribers_count']}\n"
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
