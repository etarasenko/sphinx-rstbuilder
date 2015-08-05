# -*- coding: utf-8 -*-

from .builders.rst import RstBuilder


def setup(app):
    app.add_builder(RstBuilder)
