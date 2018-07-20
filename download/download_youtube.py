import os, re, sys
import unicodedata
import subprocess
import pytube

def DownloadYoutube(url):
    try:
        if not os.path.isdir(".\\videos"):
            os.mkdir(".\\videos")

        yt=pytube.YouTube(url)
        vids=yt.streams.all()

        parent_dir=".\\videos"
        vids[0].download(parent_dir)

        new_filename=re.findall("watch\?v=(\S+)", url)[0]+".mp4"
        default_filename=vids[0].default_filename
        try:
            os.rename(os.path.join(parent_dir, default_filename), os.path.join(parent_dir, new_filename))
        except FileExistsError as e:
            print(new_filename, "파일이 존재합니다.")
            os.remove(os.path.join(parent_dir, default_filename))
    except Exception as e:
        print(e)
# end def

if __name__ == "__main__":
    DownloadYoutube(sys.argv[1])