#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: run.py
Author: huxuan, Francis Chan
Email: i(at)huxuan.org, f1ancis621@gmail.com
Description: run script file
"""
import sys

from app import app


def main():
    if sys.argv[0] != 'uwsgi':
        app.debug = True
    app.run()

if __name__ == '__main__':
    main()