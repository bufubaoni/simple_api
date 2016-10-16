#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, Bottle, response, json_dumps, post
import bottle
from beaker.middleware import SessionMiddleware
from config.sesion_config import sesion_config
from bottle_rest import json_to_params
import pdb
app = bottle.default_app()
blog = SessionMiddleware(app, sesion_config)


@route("/")
@json_to_params
def index():
    # pdb.set_trace()
    response.add_header(name="Access-Control-Allow-Origin",
                        value="http://127.0.0.1")
    return {"title": "index",
            "content": "welcome to my blog"}


@route("/topiclist")
@json_to_params
def topiclist():
    response.add_header(name="Access-Control-Allow-Origin",
                        value="http://127.0.0.1")
    return [{"id": 1,
                        "title": "this is title 1"},
                       {"id": 2,
                        "title": "this is title 2"}]


@route("/topic/<topicid:int>")
@json_to_params
def topic(topicid=None):
    # response.add_header(name="Access-Control-Allow-Origin",
    #                     value="http://127.0.0.1")
    topic = {"topic": "<h2>this is topic {topicid}</h2>".format(topicid=topicid),
             "title": "title"}
    return topic


@post("/test", "post")
@json_to_params
def test(*args, **kwargs):
    return [{"id": 1,
             "title": "this is title 1"},
            {"id": 2,
             "title": "this is title 2"}]


if __name__ == "__main__":
    bottle.run(app=blog, host="127.0.0.1", reloader=True, port=8001)
