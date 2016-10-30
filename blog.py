#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, response, post, request, json_dumps
import bottle
from beaker.middleware import SessionMiddleware
from config.sesion_config import sesion_config
from bottle_rest import json_to_params
from com.restful import restfull

app = bottle.default_app()
blog = SessionMiddleware(app, sesion_config)


@route("/")
@restfull(name="Access-Control-Allow-Origin",
          value="http://127.0.0.1")
def index():
    return {"title": "index",
            "content": "welcome to my blog"}


@route("/topiclist")
@restfull(name="Access-Control-Allow-Origin",
          value="http://127.0.0.1")
def topiclist():
    # response.add_header(name="Access-Control-Allow-Origin",
    #                     value="http://127.0.0.1")
    # response.content_type = "application/json; charset=utf-8"

    return [{"id": 1,
             "title": "this is title 1"},
            {"id": 2,
             "title": "this is title 2"}]


@route("/topic/<topicid:int>")
@restfull(name="Access-Control-Allow-Origin",
          value="http://127.0.0.1")
def topic(topicid=None):
    topic = {"topic": ("<div class='ui segment'>"
                       "<p>ttt{topicid}</p>"
                       "</div>").format(topicid=topicid),
             "title": "title"}
    return topic


@post("/login")
@route("/login", method=["OPTIONS", "GET"])
@restfull(name="Access-Control-Allow-Origin",
          value="http://127.0.0.1",
          methods="POST",
          headers="Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token")
def login():
    if request.method == "POST":
        return {"sessionid": request.json.get("username")}

    return {"sessionid": "ok"}


# @post("/adduser")
# def adduser():
#     return {""}


if __name__ == "__main__":
    bottle.run(app=blog, host="127.0.0.1", reloader=True, port=8001)
