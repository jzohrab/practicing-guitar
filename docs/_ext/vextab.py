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

from docutils import nodes
from docutils.parsers.rst import directives, Directive
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

    # Add "tabstave notation=true" if it's not there already.
    if ("tabstave" not in rawcontent):
        rawcontent = "tabstave notation=true\n   notes {0}".format(rawcontent)
    if ("options" not in rawcontent):
        rawcontent = "options space=20 scale=0.85 font-style=italic\n{0}".format(rawcontent)

    width = 800
    if ('width') in node:
        width = node['width']

    finalcontent = """<div class="vextab-auto" width={1}>
{0}
</div>""".format(rawcontent, width)
    print(finalcontent)
    self.body.append(finalcontent)

    if node['example'] is not None:
        examplediv = """<div class="vextabexample" width={1}>
<a href="#" onclick="startPlayExample('{0}');">&#9654; Play sample</a>
</div>""".format(node['example'], width)
        self.body.append(examplediv)


def depart_vextab_node(self, node):
    pass

def unsupported_visit_vextab(self, node):
    self.builder.warn('vextab: unsupported output format (node skipped)')
    raise nodes.SkipNode


class VextabDirective(Directive):
    has_content = True
    # required_arguments = 1
    # optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "width": directives.unchanged,
        "example": directives.unchanged
    }

    def run(self):
        content = self.content
        width = self.options.get('width', 800)
        example = self.options.get('example', None)
        return [vextab(content=self.content, width=width, example=example)]


_NODE_VISITORS = {
    'html': (visit_vextab_html, depart_vextab_node),
    'latex': (unsupported_visit_vextab, None),
    'man': (unsupported_visit_vextab, None),
    'texinfo': (unsupported_visit_vextab, None),
    'text': (unsupported_visit_vextab, None)
}


def setup(app):
    app.add_node(vextab, **_NODE_VISITORS)
    app.add_directive("vextab", VextabDirective)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
