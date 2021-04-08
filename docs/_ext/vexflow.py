# Custom extension for writing vexflow
#
# Vexflow needs to be written to an html div.  In rst, this looks like this:
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
# .. vexflow::
#    :notes: =|: :16 5u/1 8d/2 5u/1 8d-6u-5d-6u-8d/2 =:|

from docutils import nodes
from docutils.parsers.rst import directives, Directive


class vexflow(nodes.General, nodes.Element): pass


def visit_vexflow_html(self, node):
    print('visiting node')
    notes = node["notes"]
    content = """   <div class="vextab-auto" width=680>
   options space=10 font-style=italic font-size=10 scale=0.75
   tabstave notation=true
   notes {notes}
   text :w, BPM = Ridiculous
   options space=40
   </div>
""".format(notes)
    self.body.append(content)

def depart_vexflow_node(self, node):
    pass

def unsupported_visit_vexflow(self, node):
    self.builder.warn('vexflow: unsupported output format (node skipped)')
    raise nodes.SkipNode


class VexflowDirective(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "notes": directives.unchanged_required
    }

    def run(self):
        notes = self.options["notes"]
        return [vexflow(id=self.arguments[0], notes=notes)]


_NODE_VISITORS = {
    'html': (visit_vexflow_html, depart_vexflow_node),
    'latex': (unsupported_visit_vexflow, None),
    'man': (unsupported_visit_vexflow, None),
    'texinfo': (unsupported_visit_vexflow, None),
    'text': (unsupported_visit_vexflow, None)
}


def setup(app):
    app.add_node(vexflow, **_NODE_VISITORS)
    app.add_directive("vexflow", VexflowDirective)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
