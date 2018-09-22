import os, sys
from moviepy.editor import *

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("비디오 디렉토리와 오디오 디렉토리를 입력하세요")
        sys.exit()
	
    if sys.argv[2] not in os.listdir():
        os.mkdir(sys.argv[2])
    if "data" not in os.listdir(".\\"+sys.argv[2]):
        os.mkdir(os.path.join(sys.argv[2], "data"))

    files=list(filter(lambda x: os.path.splitext(x)[1] == ".mp4" ,os.listdir(sys.argv[1])))
    for filename in files:
        try:
            video_clip=VideoFileClip(os.path.join(sys.argv[1], filename))
            audio_clip=video_clip.audio
            print("\npath:", ".\\"+os.path.join(sys.argv[1], "data\\"+filename))
            audio_clip.write_audiofile(os.path.join(sys.argv[2], "data\\"+os.path.splitext(filename)[0]+".wav"))
            audio_clip.close()
	    video_clip.close()
        except Exception as e:
            print(filename, e)
