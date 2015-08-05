# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.utils import column_width
from sphinx.writers.text import TextTranslator, TextWriter


class RstWriter(TextWriter):
    supported = ('rst', )

    def __init__(self, builder):
        TextWriter.__init__(self, builder)
        self.translator_class = self.builder.translator_class or RstTranslator


class RstTranslator(TextTranslator):

    def new_state(self, indent=4):
        TextTranslator.new_state(self, indent)

    def visit_bullet_list(self, node):
        if len(self.list_counter):
            self.new_state(0)
            self.add_text(self.nl)
        self.list_counter.append(-1)

    def depart_bullet_list(self, node):
        self.add_text('')
        self.list_counter.pop()
        if len(self.list_counter):
            self.add_text(self.nl)
            self.end_state()

    def visit_desc_content(self, node):
        self.new_state(0)
        self.add_text(self.nl)

    def visit_desc_signature(self, node):
        self.new_state(0)
        if node.parent['objtype'] in ('class', 'exception',
                                      'method', 'function'):
            self.add_text('**')
        else:
            self.add_text('``')

    def depart_desc_signature(self, node):
        if node.parent['objtype'] in ('class', 'exception',
                                      'method', 'function'):
            self.add_text('**')
        else:
            self.add_text('``')
        text = ''.join(x[1] for x in self.states.pop() if x[0] == -1)
        self.states.append(
            [(0, ['', text, '-' * column_width(text)])])
        self.end_state()

    def depart_list_item(self, node):
        if self.list_counter[-1] == -1:
            self.end_state(first='* ', end=None)
        elif self.list_counter[-1] == -2:
            pass
        else:
            self.end_state(first='%s. ' % self.list_counter[-1])

    def visit_literal(self, node):
        self.add_text('``')

    def depart_literal(self, node):
        self.add_text('``')

    def visit_literal_block(self, node):
        last = self.states[-1][-1]
        if last[1][-2].endswith(':'):
            last[1][-2] = last[1][-2] + ':'
        else:
            self.add_text('::')
        self.new_state()

    def visit_reference(self, node):
        if 'name' not in node and 'internal' not in node:
            return
        self.add_text('`%s <%s>`_' % (node.astext(), node['refuri']))
        raise nodes.SkipNode
