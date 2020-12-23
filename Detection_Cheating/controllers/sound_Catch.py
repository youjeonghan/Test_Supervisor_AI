import io
import os
import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import math
from pydub import AudioSegment
#pydub 그냥인스톨하면 에러남 인스톨 방법 업로드해놓음

# Imports the Google Cloud client library
from google.cloud import speech

# FILE_PATH="C://Users/82109/stt/"
# FILE_NAME="Han03.wav"

# 여유값 +- 1초 함수
def catchZone(second_list):
	output = []
	s = second_list[0] - 1 if second_list[0] - 1 >= 0 else 0
	e = second_list[0] + 1
	for sec in second_list[1:]:
		if e >= sec - 1:
			e = sec + 1
			continue
		else:
			output.append((s, e))
			s = sec - 1
			e = sec + 1
	
	output.append((s, e))

	#print('time_zone(start, end):   ', output, '/n')
	return output

#speech 부분 캐치하는 함수
def catchVoice(FILE):
	samplerate, data = sio.wavfile.read(FILE)
	times = np.arange(len(data))/float(samplerate)

	# wav 2channel 이라서 1channel로 바꿔줌
	(bottom, top) = np.hsplit(data, 2)
	flatten_bottom = bottom.flatten()
	flatten_top = top.flatten()

	# soundwave 특이점 추출(second 단위)
	flatten_top_times = len(flatten_top[::100])
	sec_list = []
	for i, v in enumerate(list(flatten_top[::100])):
		gauge = abs(int(v)) // 100	# 잡음 제거
		if gauge == 0:
			continue
		else:
			t = times[-1] * (i + 1) / flatten_top_times
			
			if math.floor(t) not in sec_list:
				sec_list.append(math.floor(t))

	#print('time_list(sec):   ', sec_list)
	#print ('time:   ', round(times[-1], 2))

	return {
		'time_list': sec_list,
		'all': round(times[-1], 2)
	}

#speech time 반환 함수
def catchVoiceTimeZone2(file_path, file_name):
	a = catchVoice(file_path + file_name)
	b = catchZone(a['time_list'])
	return {
		'all_time': a['all'],
		'time_zone': b
	}
  
# wav to flac 변환 함수->
def wav2flac(WAV_FILE, time_list):
    #wav파일 경로 중 파일명만 잘라서 .flac과 결합
    song = AudioSegment.from_wav(WAV_FILE)
    FLAC_FILE = []
    for i in range(len(time_list)):
         #분할될 파일 이름 설정
        FLAC_FILE.append(os.path.splitext(WAV_FILE)[0]+ "_" + str(i) + ".flac")
        start = time_list[i][0] * 1000
        end = time_list[i][1] * 1000
         #wav파일 열기
        song = AudioSegment.from_wav(WAV_FILE)
         #section 분할
        speech_section = song[start: end]

         #채널변경 stereo->mono
        speech_section = speech_section.set_channels(1)
        
         #파일 변환 파라미터(파일명(확장자포함돼야함) , format = "확장자")
        speech_section.export(FLAC_FILE[i], format = "flac")
       
#speech to text
def speech_to_text(FLAC_FILE):
    text = []
    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    SPEECH_FILE = FLAC_FILE

    #오디오파일 메모리에 로드
    with io.open(SPEECH_FILE, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)        

    config = speech.RecognitionConfig(
    language_code="ko-KR",
    )
    #오디오 파일에서 speech감지
    response = client.recognize(config=config, audio=audio)

    #결과 출력 (리턴으로 바꿔주기~)
    for result in response.results:
        text.append((result.alternatives[0].transcript))

    return text

#stt 호출함수
def call_stt(FILE_PATH, time_list):
    text = []
    speech_section_path = []

    for i in range(len(time_list)):
        speech_section_path.append(os.path.splitext(FILE_PATH)[0]+ "_" + str(i) + ".flac")
        text.append(speech_to_text(speech_section_path[i]))
    
    #print("final", text)
    return text