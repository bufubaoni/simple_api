#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, Bottle, response, json_dumps
import bottle
from beaker.middleware import SessionMiddleware
from config.sesion_config import sesion_config

app = bottle.default_app()
blog = SessionMiddleware(app, sesion_config)


@route("/")
def index():
    response.add_header(name="Access-Control-Allow-Origin",
                        value="http://127.0.0.1:8000")
    return dict({"title": "index",
                 "content": "welcome to my blog"})


@route("/topiclist")
def topiclist():
    response.add_header(name="Access-Control-Allow-Origin",
                        value="http://127.0.0.1:8000")
    return json_dumps([{"id": 1,
                        "title": "this is title 1"},
                       {"id": 2,
                        "title": "this is title 2"}])


@route("/topic/<topicid:int>")
def topic(topicid=None):
    response.add_header(name="Access-Control-Allow-Origin",
                        value="http://127.0.0.1:8000")
    topic={"topic": "this is topic {topicid}".format(topicid=topicid)}
    return topic


if __name__ == "__main__":
    bottle.run(app=blog, host="127.0.0.1", reloader=True, port=8001)
