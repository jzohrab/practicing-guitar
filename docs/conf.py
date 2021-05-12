# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# Add custom extensions
# ref https://www.sphinx-doc.org/en/master/development/tutorials/helloworld.html
import os
import sys
sys.path.append(os.path.abspath("./_ext"))
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'Practicing Guitar'
copyright = '2021, Jeff Zohrab'
author = 'Jeff Zohrab'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',
    'ytsphinx.youtube',
    'sphinx_rtd_theme',

    # custom code in _ext/
    'vextab',
    'technique',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    # 'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': None,
    'style_external_links': False,
    'vcs_pageview_mode': '',
    # 'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
    'includehidden': True,
    'titles_only': True
}

# Don't show the "view the source" link on top right.
html_show_sourcelink = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def setup(app):
    app.add_js_file('vextab.dev.js')
    app.add_js_file('generalstuff.js')
    app.add_css_file('override.css')

# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html
todo_include_todos = True
autosectionlabel_prefix_document = True
# todo_emit_warnings = True
