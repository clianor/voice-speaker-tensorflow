# Export Audio Chunks

### 파일 설명
- audio_Spectrum.py
    - ``` python audio_Spectrum.py ``` 처럼 사용하며 파일을 열어 librosa.load 부분을 수정하여 특정 음성 파일의 스펙트럼을 확인할 수 있습니다.
- audio_chunks.py
    - ``` python audio_chunks.py ``` 처럼 사용하며 audio_Spectrum.py와 같이 열어 함수의 인자 부분을 수정하여 사용할 수 있습니다.
- export_audioChunks.py
    - ``` python export_audioChunks.py ``` 처럼 사용하며 audios파일에 존재하는 모든 wav 파일들을 조건에 맞는 chunk로 split하여 chunks 디렉토리에 저장합니다.
* * *

### 실행 순서
1. ``` python audio_Spectrum.py ``` 처럼 사용하여 먼저 오디오의 스펙트럼을 확인한다.
2. ``` python export_audioChunks.py ``` 처럼 사용하여 오디오의 chunk들을 추출합니다.
3. ``` python audio_total_length.py ``` 처럼 사용하여 추출된 chunk들의 총 길이를 계산합니다. (단위 : sec)
* * *

### Speech to text
- 구글 Speech API를 이용 아래 참조.
    - https://cloud.google.com/speech-to-text/docs/reference/libraries?hl=ko