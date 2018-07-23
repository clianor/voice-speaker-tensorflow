import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

def AudioChuncks(filePath, format):
    if "chuncks" not in os.listdir():
        os.mkdir("chuncks")

    sound = AudioSegment.from_file(filePath, format=format)

    chunks = split_on_silence(
        sound,
        # 0.5초(500ms)보다 긴 무음을 무음으로 간주.
        min_silence_len = 500,
        # -50 dBFS 미만의 소리는 없는것으로 간주.
        silence_thresh = -50,
    )

    soundCount = 0
    for chunk in chunks:
        # 잘려진 음성의 길이가 0.8초 이상일때 사용함.
        if chunk.duration_seconds > 0.8:
            chunk.export("./chuncks/"+os.path.splitext(filePath)[0]+"{0}.wav".format(soundCount), format="wav")
            soundCount += 1

if __name__ == "__main__":
    AudioChuncks("./yVxDSnTFN6o&t=5s.wav", "wav")