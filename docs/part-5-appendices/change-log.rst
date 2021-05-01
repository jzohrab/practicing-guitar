Change Log
----------

A summary of document changes for each release.

.. todo:: when draft complete, push tag

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
   
* Initial draft publication (TODO tag here)

