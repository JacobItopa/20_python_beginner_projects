import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
duration = 10.5 #seconds

sd.default.samplerate = fs
sd.default.channels = 2
myrecording = sd.rec(int(duration * fs))

print("Recording....")
sd.wait()

recorded = "recording.wav"
write(recorded, fs, myrecording)

print("Recording is complete, check " + recorded + " file")


