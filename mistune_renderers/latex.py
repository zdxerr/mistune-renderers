"""
LatexRenderer for mistune.
"""


import mistune

BEGIN = r'\begin{%s}'
END = r'\end{%s}'

def enclose(tag, content):
    return '\n%s\n%s\n%s\n' % (BEGIN % (tag, ), content, END % (tag, ))


def escape(text):
    """Replace special characters with Latex-safe sequences."""

    text = text.replace('\\', '\\textbackslash')
    text = text.replace('&', '\\&')
    text = text.replace('%', '\\%')
    text = text.replace('$', '\\$')
    text = text.replace('#', '\\#')
    text = text.replace('_', '\\_')
    text = text.replace('{', '\\{')
    text = text.replace('}', '\\}')
    text = text.replace('~', '\\textasciitilde')
    text = text.replace('^', '\\textasciicircum')

    return text


class LatexRenderer(mistune.Renderer):
    """

    """



    def block_code(self, code, lang):
        return enclose('verbatim', code)

    def block_quote(self, text):
        return enclose('quotation', text)

    def header(self, text, level, raw=None):
        tag = 'sub' * (level - 1) + 'section' if level < 4 else 'paragraph'
        return '\\%s{%s}\n' % (tag, text)

    def list(self, body, ordered=True):
        return enclose('enumerate' if ordered else 'itemize', body)

    def list_item(self, text):
        return r'\item ' + text + '\n'

    def paragraph(self, text):
        return text + '\n\n'

    def linebreak(self):
        return '\n'

    def emphasis(self, text):
        return r'\textit{%s}' % (text, )

    def double_emphasis(self, text):
        return r'\textbf{%s}' % (text, )

    def codespan(self, text):
        return r'\texttt{%s}' % (text, )

    def hrule(self):
        return r'\hrulefill' + '\n'

    def footnotes(self, text):
        return text

    def footnote_ref(self, key, index):
        return r'\footnotemark[%s]' % (key, )

    def footnote_item(self, key, text):
        return r'\footnotetext[%s]{%s}' % (key, text)

    def reference(self, key):
        return r'\cite{%s}' % (key, )

    def text(self, text):
        return escape(text)

    def image(self, src, title, text):
       return enclose('figure', 
                      '\n'.join([r'\includegraphics{%s}' % (src, ),
                                 r'\caption{%s}' % (title, ), 
                                 r'\label{%s}' % (text, ), ]))
