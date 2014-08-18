"""
Run `LatexRenderer` tests.
"""

import os
import unittest

import mistune
from mistune_renderers import LatexRenderer

root = os.path.dirname(__file__)
base_path = os.path.join(root, 'latex')


class TestLatexRenderer(unittest.TestCase):
    def setUp(self):
        self.latex_renderer = LatexRenderer()
        self.m = mistune.Markdown(renderer=self.latex_renderer)


def generator(case):
    def test(self):
        md_path = os.path.join(base_path, '%s.md' % (case, ))
        latex_path = os.path.join(base_path, '%s.tex' % (case, ))
        with open(md_path) as md_file:
            md = md_file.read()

        with open(latex_path) as latex_file:
            expected = latex_file.read().strip()

        result = self.m.render(md).strip()

        self.assertMultiLineEqual(expected, result)
    return test


cases = [fn.rsplit('.', 1) [0] for fn in os.listdir(base_path) if fn.endswith('.md')]
for case in cases:
    setattr(TestLatexRenderer, 'test_%s' % (case, ), generator(case))


if __name__ == '__main__':
    unittest.main()
