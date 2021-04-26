# Custom extension for writing vextab
#
# Vextab needs to be written to an html div.  In rst, this looks like this:
#
# .. raw:: html
# 
#    <div class="vextab-auto" width=800>
#    options space=10 font-style=italic font-size=10 scale=0.75
#    tabstave notation=true key=Dm time=12/8
#    notes =|: :16 5u/1 8d/2 5u/1 8d-6u-5d-6u-8d/2 =:|
#    </div>
#
# This is tedious and verbose.  With this extension, the above can be written like this:
#
# .. vextab::
#
#    # This line is a comment (all lines starting with # are skipped)
#    tabstave notation=true key=Dm time=12/8
#    notes =|: :16 5u/1 8d/2 5u/1 8d-6u-5d-6u-8d/2 =:|
#
# If you don't need any addition tabstave options, just using the notes should work:
#
# .. vextab::
#
#    =|: :16 5u/1 8d/2 5u/1 8d-6u-5d-6u-8d/2 =:|
#
# Other things you can add:
#
# .. vextab::
#    :exmaple: path to audio clip
#    :debug:  (if you want to print the result to console)
from docutils import nodes
from docutils.parsers.rst import directives, Directive
from sphinx.util.docutils import SphinxDirective
from os import path
import re

class vextab(nodes.General, nodes.Element): pass


def visit_vextab_html(self, node):
    lines = [
        # Remove trailing bar: Vextab currently doesn't really like it
        # when the last notes line ends with a bar ...  See
        # https://github.com/0xfe/vextab/pull/122 for pending fix.
        # re.sub(r'\|$', '', line)
        line
        for line in [
                s
                for s in
                node['content']
                if not s.strip().startswith('#')
                ]
    ]
    rawcontent = '\n'.join(lines)

    if ("notes" not in rawcontent):
        rawcontent = "\n".join([ "notes {0}".format(s) for s in lines ])
    if ("tabstave" not in rawcontent):
        rawcontent = "tabstave notation=true\n{0}".format(rawcontent)
    if ("options" not in rawcontent):
        rawcontent = "options scale=0.85 font-style=italic\n{0}".format(rawcontent)

    width = 800
    if ('width') in node:
        width = node['width']

    # Hacky css: if we have an example, keep it close to the score.
    spacingadjustment = ''
    if node['example'] is not None:
        spacingadjustment = 'style=\"margin: 0 0 0px !important;\"'

    finalcontent = """<div class="vextab-auto" {1} width={2}>
{0}
</div>""".format(rawcontent, spacingadjustment, width)

    example = node['example']
    if example is not None and example != 'pending':
        finalcontent += """\n<div class="vextabexample" width={1}>
<button onclick="startPlayExample('{0}');">&#9654; Play sample</button>
</div>""".format(node['example'], width)

    if node['debug']:
        print("\n{0}\n".format(finalcontent))

    self.body.append(finalcontent)

def depart_vextab_node(self, node):
    pass

def unsupported_visit_vextab(self, node):
    self.builder.warn('vextab: unsupported output format (node skipped)')
    raise nodes.SkipNode


class VextabDirective(SphinxDirective):
    has_content = True
    # required_arguments = 1
    # optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "width": directives.unchanged,
        "example": directives.unchanged,
        "debug": directives.unchanged
    }

    def run(self):
        content = self.content
        width = self.options.get('width', 800)
        example = self.options.get('example', None)
        debug = 'debug' in self.options

        if example is not None and example != 'pending':
            thisdir = path.dirname(path.abspath(__file__))
            reldir = path.join(thisdir, '..', '_static', 'audio', example)
            if not path.exists(reldir):
                env = self.state.document.settings.env
                raise Exception("Vextab {1} error: Missing example {0}".format(reldir, env.docname))

        if example == 'pending':
            if not hasattr(self.env, 'vextab_pending_examples'):
                self.env.vextab_pending_examples = []
            self.env.vextab_pending_examples.append(self.env.docname)

        return [vextab(content=self.content, width=width, example=example, debug=debug)]


_NODE_VISITORS = {
    'html': (visit_vextab_html, depart_vextab_node),
    'latex': (unsupported_visit_vextab, None),
    'man': (unsupported_visit_vextab, None),
    'texinfo': (unsupported_visit_vextab, None),
    'text': (unsupported_visit_vextab, None)
}


def print_pending_examples(app, exception):
    if hasattr(app.env, 'vextab_pending_examples'):
        exs = list(set(app.env.vextab_pending_examples))
        print('\nThere are some pending examples:')
        e = [ "* {0}".format(s) for s in exs ]
        print('\n'.join(e))
        print('\n')
        

def setup(app):
    app.add_node(vextab, **_NODE_VISITORS)
    app.add_directive("vextab", VextabDirective)
    app.connect('build-finished', print_pending_examples)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
