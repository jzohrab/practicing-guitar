import docutils
from docutils import nodes
import sphinx
from docutils.parsers import rst
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive
from sphinx.domains import Domain, Index
from sphinx.domains.std import StandardDomain
from sphinx.roles import XRefRole
from sphinx.directives import ObjectDescription
from sphinx.util.nodes import make_refnode
from sphinx import addnodes


DOMAIN_NAME = 'tech'

class technique(nodes.General, nodes.Element):
    """The technique."""
    pass

def visit_technique_node(self, node):
    def append(s):
        self.body.append(s)
    
    # Use the page title ('===') as the title
    # append(self.starttag(node, "p", node["displayname"], CLASS = 'name'))
    append(self.starttag(node, "p", CLASS = 'techdesc'))
    append(self.starttag(node, "span", "Summary: ", CLASS = 'techdescintro'))
    append("</span>")
    append("{0} &nbsp; {1}".format(node["description"], node["stars"]))
    append("</p>")
    append("<hr />")

    # Note: not sure why, but the node passed here for the visit
    # didn't contain the latest node data (i.e., the 'examples'
    # added during resolve_xref).  Re-fetching that data here.
    examples = self.builder.env.get_domain(DOMAIN_NAME).get_technique(node["signature"])["examples"]
    if len(examples) > 0:
        anchors = [
            "<li><a href=\"{0}\">{1}</a></li>".format(e['uri'], e['title'])
            for e in examples
        ]
        anchors = list(set(anchors))
        anchors.sort()
        append(self.starttag(node, 'div', '', CLASS = 'techniqueexample'))
        append(self.starttag(node, 'p', 'Examples', CLASS = 'heading'))
        append("</p>")
        append(self.starttag(node, 'ul'))
        for a in anchors:
            append(a)
        append("</ul></div>")

def depart_technique_node(self, node):
    pass

def unsupported_visit_technique(self, node):
    self.builder.warn('technique: unsupported output format (node skipped)')
    raise nodes.SkipNode

_NODE_VISITORS = {
    'html': (visit_technique_node, depart_technique_node),
    'latex': (unsupported_visit_technique, None),
    'man': (unsupported_visit_technique, None),
    'texinfo': (unsupported_visit_technique, None),
    'text': (unsupported_visit_technique, None)
}


class TechniqueDirective(ObjectDescription):
    """A custom node that describes a technique."""
  
    required_arguments = 1

    option_spec = {
        'displayname': directives.unchanged_required,
        'rating': directives.unchanged,
        'status': directives.unchanged
    }

    def run(self):
        targetid = 'technique-%d' % self.env.new_serialno(DOMAIN_NAME)
        targetnode = nodes.target('', '', ids=[targetid])

        opts = self.options
        displayname = opts['displayname']

        if 'status' in opts:
            s = opts['status'].lower()
            if (s == 'todo' or s == 'pending'):
                displayname = '{0} (TODO)'.format(displayname)

        signature = self.arguments[0]
        name = '{}.{}'.format(DOMAIN_NAME, signature)
        anchor = 'technique-{}'.format(signature)

        rating = int(opts['rating']) if 'rating' in opts else 0
        star = '&#9734;'
        stars = star * rating

        r = technique(
            id = self.arguments[0],
            name = name,
            displayname = displayname,
            rating = rating,
            stars = stars,
            description = "\n".join(self.content),
            signature = signature,
            type = 'Technique',
            docname = self.env.docname,
            anchor = anchor,
            priority = 0,

            # References where this technique is linked from in examples
            examples = []
        )

        techniques = self.env.get_domain(DOMAIN_NAME)
        techniques.add_technique(r)
        return [ targetnode, r ]

    def handle_signature(self, sig, signode):
        signode += addnodes.desc_name(text=self.options['displayname'])
        # signode += addnodes.desc_type(text='Technique')
        return sig

    def add_target_and_index(self, name_cls, sig, signode):
        signode['ids'].append(DOMAIN_NAME + '-' + sig)
        if 'noindex' not in self.options:
            domain = self.env.get_domain(self.domain)
            domain.add_technique(sig, self)


class TechniquelistDirective(Directive):
    def run(self):
        return [techniquelist('')]

class techniquelist(nodes.General, nodes.Element):
    pass


def process_techniquelist_nodes(app, doctree, fromdocname):
    """Replace all techniquelist nodes with a list of the collected techniques."""
    env = app.builder.env

    domain = env.get_domain(DOMAIN_NAME)
    techniques = domain.get_techniques()

    for node in doctree.traverse(techniquelist):
        listnode = nodes.bullet_list()

        for r in techniques:
            para = nodes.paragraph()

            displayname = r['displayname']
            refnode = nodes.reference(displayname, displayname)
            refnode['refdocname'] = r['docname']
            refnode['refuri'] = app.builder.get_relative_uri(fromdocname, r['docname'])
            refnode['refuri'] += '#' + r['anchor']
            para += refnode
            t = " - {0} ".format(r['description'])
            para += nodes.Text(t, t)

            # Insert into the list
            # content.append(para)
            listnode += nodes.list_item('', para)

        node.replace_self(listnode)


class TechniqueRatingIndex(Index):
    """Techniques by rating."""
    name = 'technique-rating-index'
    localname = 'Technique Rating Index'
    shortname = 'Technique Rating'
    
    def __init__(self, *args, **kwargs):
        super(TechniqueRatingIndex, self).__init__(*args, **kwargs)

    def generate(self, docnames=None):
        """See docs in https://www.sphinx-doc.org/en/1.4.8/extdev/domainapi.html#sphinx.domains.Index.generate"""
        content = {}
        for r in self.domain.get_techniques():
            k = r['stars']
            if (k == ''):
                k = '-'
            lis = content.setdefault(k, [])
            lis.append((
                r['displayname'], 0, r['docname'], r['anchor'],
                '', '',
                r['description']
            ))

        # Hacky sorting: first sorting by the length of the key
        # (stars) in reverse order.  technique['stars'] is a string, and
        # no rating is a dash ... we're lucky because one dash sorts
        # lower than one star, so we can sort these things by the
        # length of the stars they have.
        re = [(k, sorted(v, key = lambda r: r[0]))
              for k, v in
              sorted(content.items(), key = lambda r: len(r[0]), reverse=True)]
        return (re, True)


class TechniqueIndex(Index):
    name = 'technique-index'
    localname = 'Technique Index'
    shortname = 'Technique'
    
    def __init__(self, *args, **kwargs):
        super(TechniqueIndex, self).__init__(*args, **kwargs)

    def generate(self, docnames=None):
        """See docs in https://www.sphinx-doc.org/en/1.4.8/extdev/domainapi.html#sphinx.domains.Index.generate"""
        content = {}
        for r in self.domain.get_techniques():
            key = r['displayname'][0]
            lis = content.setdefault(key, [])
            lis.append((
                r['displayname'], 0, r['docname'], r['anchor'],
                '', '',
                r['description']
            ))
        re = [(k, sorted(v, key = lambda r: r[0])) for k, v in sorted(content.items())]

        return (re, True)


class TechniqueDomain(Domain):
    name = DOMAIN_NAME
    label = 'Technique Sample'

    roles = {
        'ref': XRefRole()
    }

    directives = {
        'technique': TechniqueDirective,
        'techniquelist': TechniquelistDirective
    }

    indices = {
        TechniqueIndex,
        TechniqueRatingIndex
    }

    initial_data = {
        'techniques': []
    }

    def get_full_qualified_name(self, node):
        """Return full qualified name for a given node"""
        return "{}.{}.{}".format(DOMAIN_NAME,
                                 type(node).__name__,
                                 node.arguments[0])


    def add_technique(self, technique):
        """Add a new technique to the domain."""
        self.data['techniques'].append(technique)


    def get_techniques(self):
        return sorted(self.data['techniques'], key = lambda r: r['displayname'])

    def get_technique(self, signature):
        match = [r for r in self.data['techniques'] if r['signature'] == signature]
        return match[0]

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        """Replace the link with the human-friendly display name."""
        r = self.get_technique(target)
        # Contnode contains the link content ... this was the only way I could see to update the content.

        # We use the page title as the link content.  I tried to get
        # the page title to be loaded automatically when the directive
        # was parsed, but the solution didn't seem obvious (env.titles
        # isn't fully populated).  So, this is a lame hack to ensure
        # that things at least stay internally consistent.
        t = env.titles[r['docname']].astext()
        if r['displayname'] != t:
            raise Exception("displayname '{0}' doesn't match title '{1}'".format(r['displayname'], t))

        # If this is a link in 'examples' to a technique, add a reference.
        if ('examples' in fromdocname):
            example = {
                'exampledocname': fromdocname,
                'uri': builder.get_relative_uri(r['docname'], fromdocname),
                'title': env.titles[fromdocname].astext()
            }
            r['examples'].append(example)

        newcontnode = nodes.literal('', t, classes = contnode.get('classes'))
        return make_refnode(builder, fromdocname, r['docname'], r['anchor'], newcontnode, r['anchor'])

def setup(app):
    app.add_domain(TechniqueDomain)
    app.add_node(technique, **_NODE_VISITORS)
    app.add_node(techniquelist)

    app.connect('doctree-resolved', process_techniquelist_nodes)

    techniqueIndex = "{0}-technique-index".format(DOMAIN_NAME)
    techniqueratingIndex = "{0}-technique-rating-index".format(DOMAIN_NAME)

    labels = StandardDomain.initial_data['labels']
    labels['techniqueindex'] = (techniqueIndex, '', 'Technique Index')
    labels['techniqueratingindex'] = (techniqueratingIndex, '', 'Technique Rating Index')

    anon = StandardDomain.initial_data['anonlabels']
    anon['techniqueindex'] = (techniqueIndex, '')
    anon['techniqueratingindex'] = (techniqueratingIndex, '')

    return {'version': '0.1'}
