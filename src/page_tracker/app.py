import os
from functools import cache

from flask import Flask
from redis import Redis, RedisError

app = Flask(__name__)


@cache
def redis():
    return Redis.from_url(
        os.getenv("REDIS_URL",
                  "redis://localhost:6379"))


@app.get("/")
def index():
    try:
        page_views = redis().incr("page_views")
    except RedisError:
        app.logger.exception("Redis Error")
        return "Someting went wrong.", 500
    else:
        return f"This page has been seen {page_views} times"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
