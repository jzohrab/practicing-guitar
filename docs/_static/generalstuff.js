/**
 * General stuff.  Right?
 */


/** An audio player. */
var audio = null

/**
 * Play an audio example.  Used in the vextab directive.
 * relpath is the relpath in static/audio
 */
window.startPlayExample = function(relpath) {
  audio = new Audio()
  // audio.loop = true
  const fullpath = `/_static/audio/${relpath}`
  audio.src = fullpath
  audio.play()

  /* To stop, do something like "function stopPlay() { p.src = ''; }" */
}
