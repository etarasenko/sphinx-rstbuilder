# -*- coding: utf-8 -*-

from sphinx.builders.text import TextBuilder

from ..writers.rst import RstWriter


class RstBuilder(TextBuilder):
    name = 'rst'
    format = 'rst'
    out_suffix = '.rst'

    def get_target_uri(self, docname, typ=None):
        return docname + self.out_suffix

    def prepare_writing(self, docnames):
        self.writer = RstWriter(self)
