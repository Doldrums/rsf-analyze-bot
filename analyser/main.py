import json
import aiohttp
import asyncio
import traceback
import sys
from aiohttp import web
import cachetools
import redis
from settings import settings

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
            msg = pubsub.get_message(ignore_subscribe_messages=True)
            if not msg:
                continue

            repo = msg['data'].decode()
            print(repo)

