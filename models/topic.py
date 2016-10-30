#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydal import Field
from models import db

db.define_table("topic",
                Field('title'),
                Field('content'),
                Field('slug'),
                Field('tags', 'list:string'),
                Field('author', 'reference author'),
                Field('createon', 'datetime'),
                Field('modifyon', 'datetime'))
