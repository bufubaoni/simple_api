#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, Bottle, response, json_dumps, post
import bottle
from beaker.middleware import SessionMiddleware
from config.sesion_config import sesion_config
from bottle_rest import json_to_params
from functools import wraps

app = bottle.default_app()
blog = SessionMiddleware(app, sesion_config)


@route("/")
@json_to_params
def index():
    return {"title": "index",
            "content": "welcome to my blog"}


@route("/topiclist")
@json_to_params
def topiclist():
    return [{"id": 1,
             "title": "this is title 1"},
            {"id": 2,
             "title": "this is title 2"}]


def test(f):
    @wraps(f,assigned=)
    def z(*args, **kwargs):
        return f(*args, **kwargs)

    return z


@route("/topic/<topicid:int>")
@json_to_params
def topic(topicid=None):
    topic = {"topic": "<h2>this is topic {topicid}</h2>".format(topicid=topicid),
             "title": "title"}
    return topic


@test
def p():
    x = 1
    print x


if __name__ == "__main__":
    print p()
    bottle.run(app=blog, host="127.0.0.1", reloader=True, port=8001)
