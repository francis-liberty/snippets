#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import app
from app import db


def add_fixtures():
    db.create_all()

    db.session.commit()
    db.session.remove()


if __name__ == '__main__':
    add_fixtures()
