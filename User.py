#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import framework.Model
import framework.IntegerField
import framework.StringField


class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()
