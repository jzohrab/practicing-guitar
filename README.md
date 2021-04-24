# Guitar practice

Documentation for guitar practicing.

Written in restructuredtext (RST).

# Prereqs

Python 3


# Special directives

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

"to-do" items are indicated with the `.. todo::` directive, and output at `todo.html` using `make html`

# Project layout

`doc` - the docs

TODO: add notes about folders


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

## Autobuild

During dev it's helpful to have a separate process running that auto-rebuilds using https://github.com/executablebooks/sphinx-autobuild.

```
# in new terminal tab
source env/bin/activate
sphinx-autobuild docs docs/_build/html
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

Checkout that repo in a sibling directory, and build it (`npm run build`)

Then copy it to this project:

Run this in the top directory of this project:

```
pushd ../vextab
npm run build
popd
pushd docs/_static/
cp ../../../vextab/dist/div.prod.js vextab.prod.js
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
