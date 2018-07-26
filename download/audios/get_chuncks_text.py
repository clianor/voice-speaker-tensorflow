import io
import os
import json
from progressbar import ProgressBar

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


def getAudioText(fn):
    client = speech.SpeechClient()

    file_name = os.path.join('chuncks',fn)
    with io.open(file_name, 'rb') as audio_file:
        content=audio_file.read()
        audio=types.RecognitionAudio(content=content)

    config=types.RecognitionConfig(language_code='ko-KR')
    response=client.recognize(config, audio)
    try:
        result = response.results[0].alternatives[0].transcript
    except:
        result = ""
    return result

if __name__ == "__main__":
    bar=ProgressBar()
    data=dict()
    for fn in bar(sorted(os.listdir("chuncks"))):
        data[fn]=getAudioText(fn)

    with open("alignment.json","w") as f:
        f.write(json.dumps(data,ensure_ascii=False,indent="\t"))