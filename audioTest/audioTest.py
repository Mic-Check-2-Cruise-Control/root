# this is a test for 3560 Project
# This project will use the computer's selected input device and record for 5 seconds
# it will output the audio as test.wav
import sounddevice as sd
from scipy.io.wavfile import write

# Sample rate
rate = 44100
#time in seconds
t = 5
print("recording you ...")
recording = sd.rec(int( t * rate), samplerate = rate, channels = 2)
sd.wait()
write("test.wav", rate, recording)