# Custom extension for writing vextab
#
# Vextab needs to be written to an html div.  In rst, this looks like this:
#
# .. raw:: html
# 
#    <div class="vextab-auto" width=680>
#    options space=10 font-style=italic font-size=10 scale=0.75
#    tabstave notation=true
#    notes =|: :16 5u/1 8d/2 5u/1 8d-6u-5d-6u-8d/2 =:|
#    options space=40
#    </div>
#
# This is tedious and verbose.  With this extension, the above can be written like this:
#
# .. vextab::
#    :notes: =|: :16 5u/1 8d/2 5u/1 8d-6u-5d-6u-8d/2 =:|

from docutils import nodes
from docutils.parsers.rst import directives, Directive


class vextab(nodes.General, nodes.Element): pass


def visit_vextab_html(self, node):
    print('visiting node')
    print(node)
    notes = node['notes']
    content = """   <div class="vextab-auto" width=680>
   options space=10 font-style=italic font-size=10 scale=0.75
   tabstave notation=true
   notes {0}
   options space=40
   </div>
""".format(notes)
    self.body.append(content)

def depart_vextab_node(self, node):
    pass

def unsupported_visit_vextab(self, node):
    self.builder.warn('vextab: unsupported output format (node skipped)')
    raise nodes.SkipNode


class VextabDirective(Directive):
    has_content = False
    # required_arguments = 1
    # optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "notes": directives.unchanged_required
    }

    def run(self):
        notes = self.options["notes"]
        return [vextab(notes=notes)]


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
