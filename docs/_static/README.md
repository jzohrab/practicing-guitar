# Static assets

Some static things committed to the repo -- I prefer vendoring rather than have dependencies to external libs.

# vextab.prod.js

This is div.prod.js from vextab github repo, https://github.com/0xfe/vextab/tree/master/releases

If rebuilding vextab to account for changes to upstream master that haven't been released yet:

```
# in vextab clone:
npm run build

# back in this repo, in /docs/_static:
cp ~/Documents/Projects/vextab/dist/div.prod.js vextab.prod.js
```