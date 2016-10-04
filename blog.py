#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, Bottle, response
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
    return dict([{"id", 1,
                  "title", "this is title 1"},
                 {"id", 2,
                  "title", "this is title 2"}])


@route("/topic/<topicid:int>")
def topic(topicid=None):
    return "Thie is topic {id}".format(id=topicid)


if __name__ == "__main__":
    bottle.run(app=blog, host="127.0.0.1", reloader=True, port=8001)
