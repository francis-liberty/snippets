#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: config.py
Author: huxuan, Francis Chan
Email: i(at)huxuan.org, f1ancis621@gmail.com
Description: config file
"""
import os

SECRET_KEY = os.environ.get('SECRET_KEY') or \
    '.\81\x86\x9el~\xa0\x87.\x9e\xc9\xc4\xdb1&\xcbQ\x16\x83\xf7\x85.g'

SQLALCHEMY_DATABASE_URI = 'mysql://guwenguanzhi:guwenguanzhi@localhost/guwenguanzhi'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True