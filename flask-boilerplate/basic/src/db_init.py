#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: db_init.py
Author: Francis Chan
Email: f1ancis621@gmail.com
Description: script to create all tables
"""
from app import db

db.create_all()