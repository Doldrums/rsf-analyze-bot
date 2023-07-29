import asyncio
import os
import sys
import traceback

# regarding outer rotes
import requests
from fastapi import APIRouter, Depends, HTTPException

# regarding work with gh api
import aiohttp
from aiohttp import web
import cachetools
from gidgethub import aiohttp as gh_aiohttp
from gidgethub import routing
from gidgethub import sansio
from gidgethub import apps

githubRouter = routing.Router()
cache = cachetools.LRUCache(maxsize=500)

githubRoutes = web.RouteTableDef()

externalRouter = APIRouter(prefix='/github')

@githubRoutes.get("/", name="home")
async def handle_get(request):
    return web.Response(text="Hello !!!")


@githubRoutes.post("/github/webhook")
async def webhook(request):
    try:
        body = await request.read()
        secret = os.environ.get("GH_SECRET")
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

    installation_access_token = await apps.get_installation_access_token(
        gh,
        installation_id=installation_id,
        app_id=os.environ.get("GH_APP_ID"),
        private_key=os.environ.get("GH_PRIVATE_KEY")
    )
    repo_name = event.data["repositories"][0]["full_name"]
    url = f"/repos/{repo_name}/issues"
    response = await gh.post(
        url,
                     data={
        'title': 'Thanks for installing my bot',
        'body': 'Thanks!',
            },
        oauth_token=installation_access_token["token"]
                             )
    print(response)


@router.get('/external-connect')
def external_connect(db = Depends(get_db)):
    return APIOk(status="ok")