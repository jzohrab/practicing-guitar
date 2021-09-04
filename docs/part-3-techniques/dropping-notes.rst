Dropping Notes
--------------

.. tech:technique:: droppingnotes
   :displayname: Dropping Notes

   For polyphonic music or fingerstyle/Travis picking, play one voice steadily, and build the line in the other voice incrementally.

With polyphonic (multi-voice) music, such as in Travis picking or fingerstyle pieces, it's tempting to start slow and try to play everything, beat by beat.  This can work, but it's slow, and musically is not *quite* correct.

A better method:

1. Master each "voice" completely separately, with *correct fingering and motions*.   Each voice should be ingrained and automatic, you should be able to hold a conversation, for example, while playing each one individually.
2. Choose one voice, and play it, looping over a small section.  Then "drop in" the first note from the other voice.  Your aim is to keep the first voice going no matter what. In other words, the "dropping" of the other note should not interfere with the first voice's ongoing movement. Repeat as many times as needed to be able to drop the other note without interfering with the first voice.
3. Keep adding notes to the other voice, note-by-note, playing each one perfectly.  Always keep the first voice rock-steady!
4. When you've built the complete line, you can repeat the process, but starting with the other voice, and dropping notes from the first.

For many rock and fingerstyle songs, there's a clear bass or accompaniment, and a melody on top.  Some other pieces, like fingerstyle arrangements, can combine many independent movements or ideas, such as melody, bass, and percussive elements.  You can treat each of these like a voice, master them independently, and then drop notes from the other voice on top of it, all the while staying at your target tempo.

Why this works
^^^^^^^^^^^^^^

* You are avoiding the usual approach of joining notes (e.g., "play this note just after this one, and these two together"), and are aiming for independent co-ordination.  Also, this is more musically and conceptually correct: for polyphonic pieces, you're playing independent harmonizing voices, rather than a "succession of chords".
* Since you're always playing at the target tempo, or as close to it as you can, you're building the correct/optimal set of connections in your brain that will be usable in performance (you won't be building a mental speed wall).

Example: Travis picking
^^^^^^^^^^^^^^^^^^^^^^^

Here's a typical picking pattern (it's not as scary as the notation suggests):

.. vextab::
   :example: techniques/dropping-notes/Travis_picking.mp3

   notes :16 3/5 0/3 2/4 1/2 3/6 0/3 :8 2/4 | :16 3/5 0/3 2/4 1/2 3/6 0/3 :8 2/4
   text :w,.1,let all notes ring

Rather than look at this as one long string of notes, it's better to think of this as two voices, a bass providing a steady 8th note pulse, and an accompaniment (fingerings shown below each):

.. vextab::
   :noexample:

   options beam-rests=false scale=0.85 font-style=italic
   tabstave notation=true
   notes :16 ## :8 0/3 1/2 $1$ :8d 0/3 | :16 ## :8 0/3 1/2 $1$ :8d 0/3

   tabstave notation=true
   notes :8 3/5 $3$ 2/4 $2$ 3/6 $3$ 2/4 $2$ | 3/5 $3$ 2/4 $2$ 3/6 $3$ 2/4 $2$ 

Per the method, we'll start with the bass voice.  Each note is played with the thumb, so you'd practice this until it feels natural and automatic.  You can even practice it beyond the target tempo, to ensure that it's effortless.  Make sure you use the fretting fingering you'll use in the final rendition as well, to ensure that things can be re-integrated! [#]_


.. vextab::
   :example: techniques/dropping-notes/bass_voice.mp3
   :width: 400

   :8 3/5 $3$ 2/4 $2$ 3/6 $3$ 2/4 $2$ =:|

Repeat the same process with the melody (not shown, because it's easy).

When both feel *ingrained and automatic* up to tempo (you can do them while chatting, watching TV, etc.), keep the bass steady and up to tempo, and drop in a note from the other voice:

.. vextab::
   :width: 400
   :example: techniques/dropping-notes/bass_plus_1_melody_note.mp3
   
   options beam-rests=false scale=0.85 font-style=italic
   tabstave notation=true
   voice
   notes :16 ## 0/3 :8 T0/3
   voice
   notes :8 3/5 2/4 3/6 2/4 =:|

The bass must stay steady!  Repeat this as many times as you need until it's smooth and automatic.

Then add another note, still keeping the bass steady and up to tempo:

.. vextab::
   :width: 400
   :example: techniques/dropping-notes/bass_plus_2_melody_notes.mp3

   options beam-rests=false scale=0.85 font-style=italic
   tabstave notation=true
   voice
   notes :16 ## 0/3 :16 T0/3 1/2 :8 T1/2
   voice
   notes :8 3/5 2/4 3/6 2/4 =:|

And finally the last note, all automatic and up to tempo:

.. vextab::
   :width: 500
   :example: techniques/dropping-notes/bass_plus_3_melody_notes.mp3

   options beam-rests=false scale=0.85 font-style=italic
   tabstave notation=true
   voice
   notes :16 ## 0/3 T0/3 1/2 T1/2 0/3 :8 T0/3
   voice
   notes :8 3/5 2/4 3/6 2/4 =:|

Every step of this process should be played up to tempo, and should be kept automatic.  You're chunking everything together in your brain, but still keeping the voices distinct.

This approach avoids speed walls that you can hit if you try to slowly build up speed -- the wall usually doesn't come from the individual parts, which are often straightforward, but from the mental work in coordinating them.  By always working up to tempo, you're building the connections that you need that function at the target speed.

Example: Bach
^^^^^^^^^^^^^

Here's a more complicated example from Bach.

.. vextab::
   :example: techniques/dropping-notes/Bach,_all_voices.mp3

   tabstave notation=true
   voice
   notes :8 6/4 h7/4 :q 0/2 :8 T0/2 5/3 :q 3/2 | :q T3/2    :16 7/3 0/1 :8 6/2 :q T6/2 :q 0/1
   voice
   notes :w ##                                 | :8 ##  5/3 :8  0/2        7/4 6/4 h7/4 :q 0/2
   voice
   notes :q ## :8 0/4 7/5 :qd 3/4 :8 0/4       | :q 2/4
   voice
   notes :q 7/6 7/6 0/5 0/5                    | 4/6 0/5 7/6 4/6

Though it's not apparent from the rather messy notation, this is actually four independent voices.  Here they are on separate staves, with fingerings added below each note:

.. vextab::
   :noexample:

   options space=20 scale=0.8
   tabstave notation=true
   notes :8 6/4 $2$ h7/4 $4$ :q 0/2 :8 T0/2 5/3 $4$ :q 3/2 $2$ | :q T3/2    :16 7/3 $4$ 0/1 :8 6/2 $2$ :q T6/2 :q 0/1

   options space=20
   tabstave notation=true
   notes :q ## :8 0/4 7/5 $4$ :qd 3/4 $1$ :8 0/4               | :q 2/4 $1$ ## ## ##
   
   options space=20
   tabstave notation=true
   notes :w ##                                                 | :8 ##  5/3 $4$ :8  0/2        7/4 $4$ 6/4 $1$ h7/4 $4$ :q 0/2
   
   options space=20
   tabstave notation=true
   notes :q 7/6 $3$ 7/6 $3$ 0/5 0/5                            | 4/6 $3$ 0/5 7/6 $3$ 4/6 $1$

If you try to play the initial tab as written without breaking it down ... well, it's tough.  It's hard to keep the different lines distinct.

Applying the method, you'd first start playing each line completely separately, *using the correct fingering and motions for that voice* (otherwise you won't be able to put everything back together).

(This example is quite involved, so I'd take it bar by bar, or even beat by beat!)

Joining two voices
++++++++++++++++++

We'll start with the bottom (bass) and top (melody) voices, first mastering each independently, so we can play them without thinking.

.. vextab::
   :example: techniques/dropping-notes/bach_bass.mp3

   notes :q 7/6 7/6 0/5 0/5

.. vextab::
   :example: techniques/dropping-notes/bach_melody.mp3

   :8 6/4 $2$ h7/4 $4$ :q 0/2 :8 T0/2 5/3 $4$ :q 3/2 $2$

The top voice, on its own, feels rather odd to play because of the weird fingering and positions, but that's what's needed for everything to work.

Once those are mastered, we'll play the full measure of the bass, and just drop in the first note of the melody, playing this as often as needed until it feels automatic (likely just a few tries will do):

.. vextab::
   :width: 400
   :example: techniques/dropping-notes/bach_bass_plus_1.mp3

   voice
   notes :w 6/4
   voice
   notes :q 7/6 7/6 0/5 0/5

Then add a note, playing until it's automatic:

.. vextab::
   :example: techniques/dropping-notes/bach_bass_plus_2.mp3

   voice
   notes :8 6/4 h7/4 :hd T7/4
   voice
   notes :q 7/6 7/6 0/5 0/5

And so on, gradually chaining notes together in the top voice:

.. vextab::
   :example: techniques/dropping-notes/bach_bass_plus_3.mp3; techniques/dropping-notes/bach_bass_plus_4.mp3

   tabstave notation=true
   voice
   notes :8 6/4 h7/4 :q 0/2 :h T0/2 =:: :8 6/4 h7/4 :q 0/2 :8 T0/2 5/3 :q T5/3
   voice
   notes :q 7/6 7/6 0/5 0/5         =:: :q 7/6 7/6 0/5 0/5

Until you reach the end.  Then, depending on how you feel, you can repeat the process going the other way:

.. vextab::
   :example: techniques/dropping-notes/bach_melody_plus_1.mp3

   tabstave notation=true
   voice
   notes :8 6/4 h7/4 :q 0/2 :8 T0/2 5/3 :q 3/2
   voice
   notes :w 7/6

.. vextab::
   :example: techniques/dropping-notes/bach_melody_plus_2.mp3

   tabstave notation=true
   voice
   notes :8 6/4 h7/4 :q 0/2 :8 T0/2 5/3 :q 3/2
   voice
   notes :q 7/6 7/6 :h T7/6

and so on.

This example may feel contrived due to the simplicity of the bass line, but the tricky part here is the fingering and voice balance.  With other material, like bass-chord-melody fingerstyle arrangements with lots of rhythms, this method is great.

Adding another voice
++++++++++++++++++++

Once you have these two voices down for this measure, and can feel them working independently, you can start adding a third voices.

First, you ensure that you can play that third voice independently and automatically.

.. vextab::
   :noexample:

   :q ## :8 0/4 7/5 $4$ :qd 3/4 $1$ :8 0/4 | :w 2/4 $1$

Then you add it to the mix.  How you do that is up to you:

* Play your current two voices, and gradually drop in notes in another voice.
* Repeat the bass-and-melody process above, but use the new voice in place of the bass or melody (some piano teachers highly recommend you work on each possible voice combination, especially for Bach's counterpoint pieces)

.. note:: This may seem exhaustive, and exhausting, when you read it!  But it really works, give it a shot, small section by small section.

.. [#] I once practiced a walking bass line until it was grooving and automatic, and then realized my fingering was all wrong when I tried adding other voices.  A small waste of time.
