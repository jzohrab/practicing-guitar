Change Log
----------

A summary of document changes for each release.

.. Command to build the change log, appending to this file:

   Run the below in docs:

   pushd part-5-appendices
   echo .. as at commit `git log -n 1 --pretty=format:"%h"` >> change-log.rst
   git log <prev sha or tag>..HEAD --pretty=format:"  * %as - %s" --reverse >> change-log.rst
   popd

   or for initial entry:

   pushd part-5-appendices
   echo .. as at commit `git log -n 1 --pretty=format:"%h"` >> change-log.rst
   git log --pretty=format:"  * %as - %s" --reverse >> change-log.rst
   popd

   Then edit the output that's been appended.

* TODO date here: Initial draft publication (TODO tag here)

  * Everything is brand new, so the only thing that changed is everything.
