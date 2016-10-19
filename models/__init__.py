#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydal import DAL

db = DAL(uri='sqlite://db.sqlite', folder="Database", db_codec='UTF-8', )
