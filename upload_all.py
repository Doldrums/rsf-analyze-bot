import pandas as pd
import requests as r

urls = pd.read_csv('ml_top_repos_links.csv')['link'].values
for url in urls:
    r.post("http://158.160.6.157:11002/api/tasks", json={"repo_url": url})
