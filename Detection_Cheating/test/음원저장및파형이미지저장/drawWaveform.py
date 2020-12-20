import sys
from pydub import AudioSegment
from PIL import Image, ImageDraw

FILE_PATH = './sound/'
SAVE_PATH = './image/waveform/'
FILE_NAME = 'Han'

class Waveform(object):
	bar_count = 150
	db_ceiling = 60

	def __init__(self, filename):
		self.filename = filename

		audio_file = AudioSegment.from_file(
			self.filename, self.filename.split('.')[-1])

		self.peaks = self._calculate_peaks(audio_file)

	def _calculate_peaks(self, audio_file):
		""" Returns a list of audio level peaks """
		chunk_length = len(audio_file) / self.bar_count

		loudness_of_chunks = [
			audio_file[i * chunk_length: (i + 1) * chunk_length].rms
			for i in range(self.bar_count)]

		max_rms = max(loudness_of_chunks) * 1.00

		return [int((loudness / max_rms) * self.db_ceiling)
				for loudness in loudness_of_chunks]

	def _get_bar_image(self, size, fill):
		""" Returns an image of a bar. """
		bar = Image.new('RGBA', size, fill)

		return bar

	def _generate_waveform_image(self):
		""" Returns the full waveform image """
		bar_width = 4
		px_between_bars = 1
		offset_left = 4
		offset_top = 4

		width = ((bar_width + px_between_bars) * self.bar_count) + (offset_left * 2)
		height = (self.db_ceiling + offset_top) * 2

		im = Image.new('RGBA', (width, height), '#ffffff00')
		for index, value in enumerate(self.peaks, start=0):
			column = index * (bar_width + px_between_bars) + offset_left
			upper_endpoint = (self.db_ceiling - value) + offset_top

			im.paste(self._get_bar_image((bar_width, value * 2), '#333533'),
					 (column, upper_endpoint))
		return im

	def save(self, save_path):
		""" Save the waveform as an image """
		png_filename = save_path + self.filename.split('/')[-1]
		png_filename = png_filename[:png_filename.rfind('.')] + '.png'
		with open(png_filename, 'wb') as imfile:
			self._generate_waveform_image().save(imfile, 'PNG')
		return png_filename

# img = Waveform(FILE_PATH + FILE_NAME + '.wav')

# img_name = img.save(SAVE_PATH)

def saveWaveform(file_path, save_path, file_name):
	img = Waveform(file_path + file_name + '.wav')
	return img.save(save_path)