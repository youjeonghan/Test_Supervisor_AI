# 비대면 온라인 시험 감독관

네트워크 분석을 위한 **Pcapng 파일**과 사용자 정면 얼굴과 소리가 녹음된 **mp4 동영상 파일**을 통해서
사용자 시험기록을 분석해주는 서비스.
(인증키가 포함된 GCP서버가 삭제되어 STT기능은 현재 되지않습니다.)

- Google STT
- EyeTracker Opensource 
  [ https://github.com/antoinelame/GazeTracking ]
- Eyetracking 결과에 따른 자체 Pass, Non-Pass 분류 AI 모델

![첨부사진](https://user-images.githubusercontent.com/47492535/103072108-4ff3ea00-4608-11eb-9c0c-1eca61b2ed31.png)

![KakaoTalk_20201222_183947979](https://user-images.githubusercontent.com/57481424/103277087-8f0cab80-4a0b-11eb-9774-44854d23dbc3.png)
**👉 시작 화면**



![KakaoTalk_20201222_194935980](https://user-images.githubusercontent.com/57481424/103277279-03dfe580-4a0c-11eb-9490-7238ca02f2a8.png)
**👉 관리자 화면**



  ## Client Server - How to run?

  ```shell
// yarn 또는 npm을 사용합니다.

yarn install // 필요 패키지를 설치합니다.
   
yarn start // HMR(Hot Module Replacement)이 가능한 개발 서버를 실행합니다.(기본포트:3000)
yarn test // .test.js로 끝나는 파일을 대상으로 테스트를 진행합니다.
yarn build // 작성한 코드를 대상으로 빌드과정을 진행합니다.
  ```

 

  ## Backend Server - How to run?

  ```shell
// python을 사용합니다.

pip install -r requirments.txt	// 필요 패키지를 설치합니다.
python app.py	// app.py를 실행합니다.
  ```

 



