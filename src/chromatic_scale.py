import raw_audio as audio

def pitch_to_freq(index, octave):
  pitch = octave + (index/12)
  freq = 55 * (2**pitch)
  return freq

def play_pitch(index, octave, duration):
  audio.play_freq(pitch_to_freq(index, octave), duration)

if __name__=='__main__':
  #test

  while True:
    index = int(input('Index: '))
    octave = int(input('Octave: '))
    duration = int(input('Duration: '))
  
    play_pitch(index, octave, duration)
