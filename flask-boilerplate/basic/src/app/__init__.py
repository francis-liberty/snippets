#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: __init__.py
Author: huxuan, Francis Chan
Email: i(at)huxuan.org, f1ancis621@gmail.com
Description: init file for app
"""
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from app import models
from app import api