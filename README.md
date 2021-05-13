# Guitar practice

Documentation for guitar practicing.

Written in restructuredtext (RST).

# Prereqs

Python 3
enchant (for spelling) - see https://pyenchant.github.io/pyenchant/install.html

# Special directives and notes

## YouTube

The `youtube::` directive embeds a video in the HTML, eg:

```
.. youtube:: -NVHoHPUAmM
   :width: 640
   :height: 480
```

## Adding TAB and notation

We use [Vextab](https://vexflow.com/vextab/).  The project includes Vextab's [div.prod.js](https://github.com/0xfe/vextab/blob/master/releases/div.prod.js) in html pages.

Use [the Vextab tutorial](https://vexflow.com/vextab/tutorial.html) to work out the music data, and then use the custom `vextab` directive to embed it in a page, e.g.:

```
.. vextab::

   =|: :16 5u/1 8d/2 5u/1 8d-6u-5d-6u-8d/2 =:|
```

See `docs/_ext/vextab.py` for other examples and notes.

## To-do items

ref: https://www.sphinx-doc.org/en/master/usage/extensions/todo.html

## Links

Linking to other .rst pages:

* If the other page has a label defined with `.. _reading-rhythms:`, you can do this:

```
Here is a link :ref:`reading-rhythms`
```

If the other page doesn't have a label, these work:

```
# Use the page heading
:ref:`theory/reading-rhythms:Reading rhythms`

# Use relative path to get to doc
:doc:`../theory/reading-rhythms`

# Link to specific heading
:ref:`theory/reading-rhythms:The Basics`
```


"to-do" items are indicated with the `.. todo::` directive, and output at `todo.html` using `make html`

## Blockquotes

Put three spaces in front, and then a link at the end followed by *2 underscores*.  eg:

```
   Text `name, source <http>`__
```

# Project layout

```
$ pushd docs; tree -d -I '_build|__pycache__'; popd

.
├── _ext  # custom extensions for directives (eg 'vextab')
├── _static
│   ├── audio  # audio files for examples
│   └── img  # images
├── _templates  # overrides for header, footer
├── examples  # example licks
├── scores  # music
├── techniques  # the actual techniques
└── theory  # how to read music, etc

```

# Development

## Setup

```
... clone and cd to the project directory

# Activate the virtual env
source env/bin/activate
# or '.\env\Scripts\activate' for Windows

# Verify
which python
# or 'where python' for Windows

# Install requirements
pip3 install -r requirements.txt

# work work work

deactivate
```

## rst headings

If under and overline are used, their length must be identical. The length of the underline must be at least as long as the title itself.

Conventions:

```
##########
Part
##########

*********
Chapter 1
*********

Section 1
=========

Subsection
----------

Subsubsection
^^^^^^^^^^^^^
```

## todos

List all todos:

```
make todos
```

## Autobuild

During dev it's helpful to have a separate process running that auto-rebuilds using https://github.com/executablebooks/sphinx-autobuild.

```
# in new terminal tab in root
source env/bin/activate
./startdevsite.sh
```

Then open http://127.0.0.1:8000 and you'll see the docs.

## Adding dependencies

If you add something, freeze it:

```
pip3 install ytsphinx   # e.g.
pip3 freeze > requirements.txt
git add requirements.txt
git commit -m "Added ytsphinx"  # e.g.
```

## Custom Vextab fork

Vextab is great, but there are a few small tweaks needed.

The changes are in https://github.com/jzohrab/vextab/tree/practicing-guitar-patched

Checkout that repo in a sibling directory, and build it (`npm run build-dev`)

Then copy the dev js to this project:

Run this in the top directory of this project:

```
pushd ../vextab
npm run build-dev
popd
pushd docs/_static/
cp ../../../vextab/dist/div.dev.js vextab.dev.js
popd
git status
pushd docs
make clean html
popd
```


## Building

```
cd docs
make html

# or:
# make clean html
```

## Building to check spelling
```
cd project-root
sphinx-build -b spelling docs docs/_build/
