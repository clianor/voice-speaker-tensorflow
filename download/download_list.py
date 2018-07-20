import os
from download_youtube import DownloadYoutube

if __name__ == "__main__":
    try:
        with open("urlList.txt", "r") as f:
            urls=f.readlines()

        for url in urls:
            DownloadYoutube(url)
    except Exception as e:
        print(e)