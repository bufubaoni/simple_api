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
    response.add_header(name="Access-Control-Allow-Origin", value="http://127.0.0.1:8000")
    return dict({"title": "index",
                 "content": "welcome to my blog"})


@route("/topiclist")
def topiclist():
    return "This is topiclist"


if __name__ == "__main__":
    bottle.run(app=blog, host="127.0.0.1", reloader=True, port=8001)
