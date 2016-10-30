#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydal import Field
from models import db

db.define_table("author",
                Field('nickname'),
                Field('email'),
                Field('avatar'),
                Field('group', 'integer'),
                Field('createon', 'datetime'))
