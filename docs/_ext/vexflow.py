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
from docutils.parsers.rst import Directive


class Vexflow(Directive):

    def run(self):
        paragraph_node = nodes.paragraph(text='content here')
        return [paragraph_node]


def setup(app):
    app.add_directive("vexflow", Vexflow)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
