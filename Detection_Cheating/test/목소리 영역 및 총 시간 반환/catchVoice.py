import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import math

FILE_PATH = './sound/'
FILE_NAME = 'micTest.wav'

# 여유값 +- 1초
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

	print('time_zone(start, end):   ', output, '\n')
	return output

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
		gauge = abs(int(v)) // 600	# 잡음 제거
		if gauge == 0:
			continue
		else:
			t = times[-1] * (i + 1) / flatten_top_times
			
			if math.floor(t) not in sec_list:
				sec_list.append(math.floor(t))

	print('time_list(sec):   ', sec_list)
	print ('time:   ', round(times[-1], 2))

	return {
		'time_list': sec_list,
		'all': round(times[-1], 2)
	}

def catchVoiceTimeZone(file_path, file_name):
	a = catchVoice(FILE_PATH + FILE_NAME)
	b = catchZone(a['time_list'])
	return {
		'all_time': a['all'],
		'time_zone': b
	}

catchVoiceTimeZone(FILE_PATH, FILE_NAME)