# Data download & Export wav files

### 파일 설명
- download_youtube.py
    - ``` python download_youtube.py <url> ``` 처럼 사용하며 유튜브 영상을 다운로드 가능합니다.
    - 저장은 videos 폴더에 저장이되면 폴더가 존재하지 않으면 만들어 저장합니다.
- download_list.py
    - ``` python download_list.py ``` 처럼 사용하며 urlList.txt 파일을 읽어 저장된 URL들의 유튜브 영상을 다운로드합니다.
- convert_wav.py
    - ``` python convert_wav.py videos audios ``` 처럼 사용하며 영상에서 오디오를 추출하여 audios 디렉토리에 저장합니다.

* * *

### 실행순서
1. ``` python download_list.py ```
2. ``` python convert_wav.py```

* * *