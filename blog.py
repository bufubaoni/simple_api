#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, Bottle, response, json_dumps, post, request
import bottle
from beaker.middleware import SessionMiddleware
from config.sesion_config import sesion_config
from bottle_rest import json_to_params
from functools import wraps, partial

app = bottle.default_app()
blog = SessionMiddleware(app, sesion_config)
globals()["session"] = request.environ.get("beaker.session")


@route("/")
@json_to_params
def index():
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
    response.add_header(name="Access-Control-Allow-Origin",
                        value="http://127.0.0.1")
    topic = {"topic": ("<div class='ui segment'>"
                       "<p>ttt{topicid}</p>"
                       "</div>").format(topicid=topicid),
             "title": "title"}
    return topic


@post("/login")
@route("/login", method=["OPTIONS", "GET"])
def login():
    response.add_header(name="Access-Control-Allow-Origin",
                        value="http://127.0.0.1")
    response.add_header(name="Access-Control-Allow-Methods",
                        value="POST")
    response.add_header(name="Access-Control-Allow-Headers",
                        value='Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token')
    session = request.environ.get("beaker.session")
    if request.method == "POST":
        return {"sessionid":request.json.get("username")}

    # if request.body.json.get("username") == "Alex":
    #     response.add_header(name="Access-Control-Allow-Origin",
    #                         value="http://127.0.0.1")
    #     response.add_header(name="Access-Control-Allow-Methods",
    #                         value="POST")
    #     response.add_header(name="Access-Control-Allow-Headers",
    #                         value='Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token')
    #     session["username"] = "Alex"
    #     return {"username": "Alex"}
    return {"sessionid": "ok"}


if __name__ == "__main__":
    bottle.run(app=blog, host="127.0.0.1", reloader=True, port=8001)
