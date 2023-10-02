from app.github import views
import json
import aiohttp
import asyncio
import traceback
import sys
from aiohttp import web
import cachetools
import redis
from gidgethub import aiohttp as gh_aiohttp
from gidgethub import routing
from gidgethub import sansio
from gidgethub import apps
from models.repo import Repo
from app.settings import settings
from db import get_db

REDIS_ML_CHNNEL = "repo_processor"

githubRouter = routing.Router()
cache = cachetools.LRUCache(maxsize=500)

routes = web.RouteTableDef()

redis = redis.Redis(
    host=settings.REDIS_HOST, 
    port=6379, 
    db=0
)

@routes.post("/github/webhook")
async def webhook(request):
    try:
        body = await request.read()
        secret = settings.GH_SECRET
        event = sansio.Event.from_http(request.headers, body, secret=secret)
        if event.event == "ping":
            return web.Response(status=200)
        async with aiohttp.ClientSession() as session:
            gh = gh_aiohttp.GitHubAPI(session, "demo", cache=cache)

            await asyncio.sleep(1)
            await githubRouter.dispatch(event, gh)
        try:
            print("GH requests remaining:", gh.rate_limit.remaining)
        except AttributeError:
            pass
        return web.Response(status=200)
    except Exception as exc:
        traceback.print_exc(file=sys.stderr)
        return web.Response(status=500)


@githubRouter.register("installation", action="created")
async def repo_installation_added(event, gh, *args, **kwargs):
    installation_id = event.data["installation"]["id"]
    print(f"repo_installation_added succeed, installation_id={installation_id}")
    installation_access_token = await apps.get_installation_access_token(
        gh,
        installation_id=installation_id,
        app_id=settings.GH_APP_ID,
        private_key=settings.GH_PRIVATE_KEY
    )

    for repo in event.data["repositories"]:
        repo_name = repo["full_name"]
        url = f"/repos/{repo_name}/issues"
        try:
            response = await gh.post(
                url,
                data={
                    'title': 'RSF Code Analyzer Report',
                    'body': '''
**Welcome to RSF Code Analyzer! 🚀**

Thank you for choosing RSF Code Analyzer and joining us on a journey towards better code quality and smoother development processes. 🙌

Who are we? We are a team dedicated to enhancing your software development experience. RSF Code Analyzer, short for "Repository Software Feedback Code Analyzer," is here to support you in identifying areas of improvement within your codebase. Our mission is to make your coding journey more efficient and your final product top-notch. 🛠️📊

Exciting news! The analysis of your repository has already commenced. Our diligent bot is hard at work gathering valuable insights and metrics to provide you with actionable suggestions for refining your codebase. ✨🔍

In the coming days, you can expect to see a range of suggestions aimed at boosting the quality of your code and streamlining your development process. We're all about continuous improvement and making your work as seamless as possible. 🌟🔧

Thank you once again for choosing RSF Code Analyzer. Your commitment to code excellence is truly commendable, and we're here to support you every step of the way. Stay tuned for updates and keep coding brilliantly! 💻🌈

Best regards,
The RSF Code Analyzer Team
                    '''
                },
                oauth_token=installation_access_token["token"]
            )
            print(response)
        except:
            print("gidgethub.BadRequest: Issues are disabled for this repo")
            continue

        db_repo = Repo(
            username="test-user",
            repo_url=response['repository_url'],
            issue_id=response['url'],
            installation_token = installation_access_token["token"],
            data=json.dumps(response),
        )

        for db in get_db():
            db.add(db_repo)
            db.commit()
            db.refresh(db_repo)

        redis.publish(REDIS_ML_CHNNEL, db_repo.id)

    return web.Response(status=200)

def setup_routes(app):
    print(f"setup_routes succeed")
    app.router.add_routes(routes)
    app.router.add_get("/external-invite", views.external_invite)
    app.router.add_get("/", views.index)
