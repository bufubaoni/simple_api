#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import request, response
import pdb


def restfull(name, value, methods="", headers=""):
    # pdb.set_trace()
    def rest(f):
        def invock(*args, **kwargs):
            response.add_header(name=name, value=value)
            if response.content_type != "application/json; charset=utf-8":
                response.content_type = "application/json; charset=utf-8"
            if methods:
                response.add_header(name="Access-Control-Allow-Methods", value=methods)
            if headers:
                response.add_header(name="Access-Control-Allow-Headers", value=headers)
            return json.dumps(f(*args, **kwargs))

        return invock

    return rest
