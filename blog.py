#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, Bottle
import bottle
from beaker.middleware import SessionMiddleware
from config.sesion_config import sesion_config
app = bottle.default_app()
blog = SessionMiddleware(app, sesion_config)


@route("/")
def index():
    return "This is index"


@route("/topiclist")
def topiclist():
    return "This is topiclist"


if __name__ == "__main__":
    bottle.run(app=blog, host="127.0.0.1", reloader=True, port=8000)
