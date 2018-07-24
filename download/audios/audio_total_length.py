import os
from os.path import splitext
from pydub import AudioSegment

audioFiles = [fileName for fileName in os.listdir("chuncks") if splitext(fileName)[1] == ".wav"]
totalLength = 0.
for fn in audioFiles:
    totalLength += AudioSegment.from_file("chuncks/"+fn, format="wav").duration_seconds

print("Audio Files Total Length :", totalLength, "sec")