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

## Building

```
cd docs
make html
```

# To-do items

ref: https://www.sphinx-doc.org/en/master/usage/extensions/todo.html

"to-do" items are indicated with the `.. todo::` directive, and output at `todo.html` using `make html`

# Project layout

`doc` - the docs

TODO: add notes about folders