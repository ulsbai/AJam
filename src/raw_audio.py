import numpy as np
import sounddevice as sd

DEFAULT_SAMPLE_RATE = 44100

def play_freq(freq, duration, sample_rate=DEFAULT_SAMPLE_RATE):
  t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
  
  audio = np.sin(2 * np.pi * freq * t)
  
  sd.play(audio, sample_rate)
  sd.wait()

if __name__=='__main__':
  #test
  while True:
    freq = int(input('Freq: '))
    duration = int(input('Duration: '))
    play_freq(freq, duration)
