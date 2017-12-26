#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View
from django.http import HttpResponse
import json


class APIView(View):
    json_engine = json

    def dispatch(self, request, *args, **kwargs):
        pass
