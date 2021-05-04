/**
 * General stuff.  Right?
 */


/** An audio player. */
var audio = null

/**
 * Play an audio example.  Used in the vextab directive.
 * path is e.g /_static/audio/whatever.mp3, where _static is determined by environment.
 */
window.startPlayExample = function(path) {
  audio = new Audio()
  // audio.loop = true
  audio.src = path
  audio.play()

  /* To stop, do something like "function stopPlay() { p.src = ''; }" */
}
