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

* 2021-05-14: First draft complete

  * Everything is brand new, so the only thing that changed is everything.

* 2021-09-24: Examples and misc. updates

  * Moved examples to :doc:`../part-4-examples/_index`

    * Added :doc:`../part-4-examples/bach-prelude-in-c-major-BWV-846`
    * Added :doc:`../part-4-examples/cliffs-of-dover-hybrid-picking`

  * :doc:`../part-2-getting-organized/time-and-schedule`

    * Added more detail about taking breaks
    * Added "20 minutes is just a suggestion"
    * Added "Don't forget fun"
  
  * :doc:`../part-3-techniques/chaining`
  
    * Added "Backwards chaining for repertoire"
    
  * :doc:`../part-3-techniques/tempo-variations`
  
    * Added "slow-fast-slow-fast" technique

  * Added :doc:`../contributing`


