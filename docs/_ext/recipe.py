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


class recipe(nodes.General, nodes.Element):
    """The recipe."""
    pass

def visit_recipe_node(self, node):
    def append(s):
        self.body.append(s)
    
    append(self.starttag(node, "div", CLASS = 'recipeheader'))
    append(self.starttag(node, "p", node["displayname"], CLASS = 'name'))
    append(self.starttag(node, "p", node["description"], CLASS = 'desc'))
    append("</p></p></div>")

    # Note: not sure why, but the node passed here for the visit
    # didn't contain the latest node data (i.e., the 'examples'
    # added during resolve_xref).  Re-fetching that data here.
    examples = self.builder.env.get_domain('rcp').get_recipe(node["signature"])["examples"]
    if len(examples) > 0:
        anchors = [
            "<li><a href=\"{0}\">{1}</a></li>".format(e['uri'], e['title'])
            for e in examples
        ]
        anchors = list(set(anchors))
        anchors.sort()
        append(self.starttag(node, 'div', '', CLASS = 'recipeexample'))
        append(self.starttag(node, 'p', 'Examples', CLASS = 'heading'))
        append("</p>")
        append(self.starttag(node, 'ul'))
        for a in anchors:
            append(a)
        append("</ul></div>")

def depart_recipe_node(self, node):
    pass

def unsupported_visit_recipe(self, node):
    self.builder.warn('recipe: unsupported output format (node skipped)')
    raise nodes.SkipNode

_NODE_VISITORS = {
    'html': (visit_recipe_node, depart_recipe_node),
    'latex': (unsupported_visit_recipe, None),
    'man': (unsupported_visit_recipe, None),
    'texinfo': (unsupported_visit_recipe, None),
    'text': (unsupported_visit_recipe, None)
}


class RecipeDirective(ObjectDescription):
    """A custom node that describes a recipe."""
  
    required_arguments = 1

    option_spec = {
        'displayname': directives.unchanged_required,
        'contains': directives.unchanged_required
    }

    def run(self):
        targetid = 'recipe-%d' % self.env.new_serialno('recipe')
        targetnode = nodes.target('', '', ids=[targetid])

        displayname = self.options['displayname']
        signature = self.arguments[0]
        name = '{}.{}'.format('recipe', signature)
        anchor = 'recipe-{}'.format(signature)
        ingredients = [x.strip() for x in self.options['contains'].split(',')]

        r = recipe(
            id = self.arguments[0],
            name = name,
            dispname = displayname,
            displayname = displayname,
            contains = self.options['contains'],

            description = "\n".join(self.content),
            ingredients = [x.strip() for x in self.options['contains'].split(',')],
            signature = signature,
            type = 'Recipe',
            docname = self.env.docname,
            anchor = anchor,
            priority = 0,

            # References where this recipe is linked from in examples
            examples = []
        )

        recipes = self.env.get_domain('rcp')
        recipes.add_recipe(r)
        return [ targetnode, r ]

    def handle_signature(self, sig, signode):
        signode += addnodes.desc_name(text=self.options['displayname'])
        # signode += addnodes.desc_type(text='Recipe')
        return sig

    def add_target_and_index(self, name_cls, sig, signode):
        signode['ids'].append('recipe' + '-' + sig)
        if 'noindex' not in self.options:
            domain = self.env.get_domain(self.domain)
            domain.add_recipe(sig, self)


class RecipelistDirective(Directive):
    def run(self):
        return [recipelist('')]

class recipelist(nodes.General, nodes.Element):
    pass


def process_recipelist_nodes(app, doctree, fromdocname):
    """Replace all recipelist nodes with a list of the collected recipes."""
    env = app.builder.env

    domain = env.get_domain('rcp')
    recipes = domain.get_recipes()

    for node in doctree.traverse(recipelist):
        listnode = nodes.bullet_list()

        for r in recipes:
            para = nodes.paragraph()

            dispname = r['dispname']
            refnode = nodes.reference(dispname, dispname)
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


class IngredientIndex(Index):
    """A custom directive that creates an ingredient matrix."""
    
    name = 'ing'
    localname = 'Ingredient Index'
    shortname = 'Ingredient'
    
    def __init__(self, *args, **kwargs):
        super(IngredientIndex, self).__init__(*args, **kwargs)

    def generate(self, docnames=None):
        """See docs in https://www.sphinx-doc.org/en/1.4.8/extdev/domainapi.html#sphinx.domains.Index.generate"""

        content = {}
        for r in self.domain.get_recipes():
            for i in r['ingredients']:
                lis = content.setdefault(i, [])
                tup = (r['dispname'], 0, r['docname'], r['anchor'], '', '', r['description'])
                lis.append(tup)
        re = [(k, v) for k, v in sorted(content.items())]
        return (re, True)


class RecipeIndex(Index):    
    name = 'rcp'
    localname = 'Recipe Index'
    shortname = 'Recipe'
    
    def __init__(self, *args, **kwargs):
        super(RecipeIndex, self).__init__(*args, **kwargs)

    def generate(self, docnames=None):
        """See docs in https://www.sphinx-doc.org/en/1.4.8/extdev/domainapi.html#sphinx.domains.Index.generate"""
        content = {}
        for r in self.domain.get_recipes():
            key = r['dispname'][0]
            lis = content.setdefault(key, [])
            lis.append((
                r['dispname'], 0, r['docname'], r['anchor'],
                '', '',
                r['description']
            ))
        re = [(k, sorted(v, key = lambda r: r[0])) for k, v in sorted(content.items())]

        return (re, True)


class RecipeDomain(Domain):
    name = 'rcp'
    label = 'Recipe Sample'

    roles = {
        'ref': XRefRole()
    }

    directives = {
        'recipe': RecipeDirective,
        'recipelist': RecipelistDirective
    }

    indices = {
        RecipeIndex,
        IngredientIndex
    }

    initial_data = {
        'recipes': []
    }

    def get_full_qualified_name(self, node):
        """Return full qualified name for a given node"""
        return "{}.{}.{}".format('rcp',
                                 type(node).__name__,
                                 node.arguments[0])


    def add_recipe(self, recipe):
        """Add a new recipe to the domain."""
        self.data['recipes'].append(recipe)


    def get_recipes(self):
        return sorted(self.data['recipes'], key = lambda r: r['displayname'])

    def get_recipe(self, signature):
        match = [r for r in self.data['recipes'] if r['signature'] == signature]
        if len(match) != 1:
            raise Exception("Bad reference, {0} matches for {1}".format(len(match), signature))
            return None
        return match[0]

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        """Replace the link with the human-friendly display name."""
        r = self.get_recipe(target)
        # Contnode contains the link content ... this was the only way I could see to update the content.

        # If this is a link in 'examples' to a recipe, add a reference.
        if ('examples' in fromdocname):
            example = {
                'exampledocname': fromdocname,
                'uri': builder.get_relative_uri(r['docname'], fromdocname),
                'title': env.titles[fromdocname].astext()
            }
            r['examples'].append(example)

        newcontnode = nodes.literal('', r['dispname'], classes = contnode.get('classes'))
        return make_refnode(builder, fromdocname, r['docname'], r['anchor'], newcontnode, r['anchor'])

def setup(app):
    app.add_domain(RecipeDomain)
    app.add_node(recipe, **_NODE_VISITORS)
    app.add_node(recipelist)

    app.connect('doctree-resolved', process_recipelist_nodes)

    StandardDomain.initial_data['labels']['recipeindex'] =\
        ('rcp-rcp', '', 'Recipe Index')
    StandardDomain.initial_data['labels']['ingredientindex'] =\
        ('rcp-ing', '', 'Ingredient Index')

    StandardDomain.initial_data['anonlabels']['recipeindex'] =\
        ('rcp-rcp', '')
    StandardDomain.initial_data['anonlabels']['ingredientindex'] =\
        ('rcp-ing', '')
    
    return {'version': '0.1'}
