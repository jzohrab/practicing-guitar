Change Log
----------

A summary of document changes for each release.

.. Command to build the change log, appending to this file:

   Run the below in docs:

   pushd part-5-appendices
   git log <prev sha or tag>..HEAD --pretty=format:"  * %as - %s" --reverse >> change-log.rst
   popd

   or for initial entry:

   pushd part-5-appendices
   git log --pretty=format:"  * %as - %s" --reverse >> change-log.rst
   popd

   Pipe that to this file, and then edit the output.

.. todo:: when draft complete, push tag, and change TODOs below

* TODO date here: Initial draft publication (TODO tag here)

  * Everything is brand new, so the only thing that changed is everything.
