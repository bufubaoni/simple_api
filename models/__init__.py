#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydal import DAL, Field

db = DAL(uri='sqlite://db.sqlite', folder="Database", db_codec='UTF-8', )

db.define_table("author",
                Field('nickname'),
                Field('email'),
                Field('avatar'),
                Field('group', 'integer'),
                Field('createon', 'datetime'))
