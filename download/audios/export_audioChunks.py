import os
from os.path import splitext
from audio_chunks import AudioChuncks

wavFiles = [fileName for fileName in os.listdir("data") if splitext(fileName)[1] == ".wav"]
for fileName in wavFiles:
    AudioChuncks(fileName, "wav")