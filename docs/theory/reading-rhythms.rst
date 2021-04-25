Reading rhythms
===============

*Just enough* notation for you to read any examples in this book.  (There's much more to this topic: ties, rests, tuples, etc.)

For the examples in the rest of this book, it's best to get a *feel* for the rhythm in your ears and hands.  Listen to the examples for each and maybe play along.  Each example has two pickup beats, followed by the measure played twice.

The Basics
**********

Quarter notes
-------------

These are quarter notes.  Each note is played for one beat.

.. vextab::
   :width: 600
   :example: theory/rhythms/quarters.mp3

   tabstave notation=true
   notes :q 0/2 $1$ 0/2 $2$ 0/2 $3$ 0/2 $4$
   text :q,.1,1,2,3,4

Eighth notes
------------

Eighth notes (8th notes) are joined by a bar.  An eighth note is half as long as a quarter note, so there are two eighth notes in one beat.

.. vextab::
   :width: 600
   :example: theory/rhythms/8ths.mp3

   tabstave notation=true
   notes :8 0/2 $1$ 0/2 $and$ 0/2 $2$ 0/2 $and$ 0/2 $3$ 0/2 $and$ 0/2 $4$ 0/2 $and$
   text :q,.1,1,2,3,4

Sixteenth notes
---------------

16th notes have a double bar.  A 16th note is half as long as an eighth, so there are four 16ths in one beat.

.. vextab::
   :width: 600
   :example: theory/rhythms/16ths.mp3

   tabstave notation=true
   notes :16 0/2 $1$ 0/2 $e$ 0/2 $and$ 0/2 $a$ 0/2 $2$ 0/2 $e$ 0/2 $and$ 0/2 $a$
   notes :16 0/2 $3$ 0/2 $e$ 0/2 $and$ 0/2 $a$ 0/2 $4$ 0/2 $e$ 0/2 $and$ 0/2 $a$
   text :q,.1,1,2,3,4

Triplets
********

Triplets fit 3 notes into the length of one beat.  Sextuplets fit 6.

Some people like different words to say for each beat ... e.g, "1-trip-let" or "1-and-uh" for triplets, instead of "1-la-li".  Use whatever works for you.

.. vextab::
   :width: 600
   :example: theory/rhythms/triplets.mp3

   tabstave notation=true
   notes :q 0/2 $1...$ 0/2 $2...$ :8 0/2 $3$ 0/2 $la$ 0/2 $li$ ^3^ 0/2 $4$ 0/2 $la$ 0/2 $li$ ^3^
   text :q,.1,1,2,3,4

.. vextab::
   :width: 600
   :example: theory/rhythms/sextuplets.mp3

   tabstave notation=true time=12/8
   notes :q 0/2 $1...$ 0/2 $2...$ :16 0/2 $3$ 0/2 $ta$ 0/2 $la$ 0/2 $ta$ 0/2 $li$ 0/2 $ta$ 0/2 $4$ 0/2 $ta$ 0/2 $la$ 0/2 $ta$ 0/2 $li$ 0/2 $ta$
   text :q,.1,1,2,3,4


Dotted rhythms
**************

Dotted rhythms are great for practicing, so be sure you get a good feel for this.

A dot after a note increases its length by half its value.  In each example below, the first two beats are straight 8th notes, and the last two have dotted eights.

Long-short
----------

.. vextab::
   :width: 600
   :example: theory/rhythms/dotted-long-short.mp3

   tabstave notation=true
   notes :8 0-0-0-0/2 :8d 0/2 $3$ :16 0/2 $a$ :8d 0/2 $4$ :16 0/2 $a$
   text :q,.1,1,2,3,4

In the above example, notice that the note after the dotted note is a regular 16th note, and it falls on the "a" of "1-e-&-a".  Here are two voices, one playing a dotted rhythm and the other playing straight 16th notes; the last note of each occurs at the same time.

.. vextab::
   :width: 600

   tabstave notation=true tablature=false
   voice
   notes :8d 0/1 :16 0/1
   voice
   notes :16 0-0-0-0/3

Short-long
----------

.. vextab::
   :width: 600
   :example: theory/rhythms/dotted-short-long.mp3

   tabstave notation=true
   notes :8 0-0-0-0/2 :16 0/2 $3$ :8d 0/2 $e$ :16 0/2 $4$ :8d 0/2 $e$
   text :q,.1,1,2,3,4

Here are two other voices, one playing a dotted rhythm and the other playing straight 16th notes; the first and second notes of each occur at teh same time.

.. vextab::
   :width: 600

   tabstave notation=true tablature=false
   voice
   notes :16 0/1 :8d 0/1
   voice
   notes :16 0-0-0-0/3

More drills
***********

There are lots of books and tutorials out there for reading rhythms.  Some I like are:

* `Modern Reading Text in 4/4 For All Instruments <https://www.amazon.com/Modern-Reading-Text-All-Instruments/dp/0769233775>`_
* `Rhythmic Training <https://www.amazon.com/Rhythmic-Training-Robert-Starer/dp/0881889768>`_
