# Guitar practice

Documentation for guitar practicing.

Written in restructuredtext (RST).

# Prereqs

Python 3



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

## Building

```
cd docs
make html
```

# Special directives

## YouTube

The `youtube::` directive embeds a video in the HTML, eg:

```
.. youtube:: -NVHoHPUAmM
   :width: 640
   :height: 480
```

## Adding TAB and notation

We use [Vextab](https://vexflow.com/vextab/).

The project includes Vextab's [div.prod.js](https://github.com/0xfe/vextab/blob/master/releases/div.prod.js) in html pages.

Use [the Vextab tutorial](https://vexflow.com/vextab/tutorial.html) to work out the music data, and then use the `raw` directive to embed it in a page, e.g.:

```
.. raw:: html

   <div class="vextab-auto" width=680>
   options space=10 font-style=italic font-size=10 scale=0.75
   tabstave notation=true
   notes =|: :16 5u/1 8d/2 5u/1 8d-6u-5d-6u-8d/2 =:|
   text :w, BPM = Ridiculous
   options space=40
   </div>
```

(In future, we make make a custom `.. vextab::` directive to simplify this, but for now this suffices).


## To-do items

ref: https://www.sphinx-doc.org/en/master/usage/extensions/todo.html

"to-do" items are indicated with the `.. todo::` directive, and output at `todo.html` using `make html`

# Project layout

`doc` - the docs

TODO: add notes about folders