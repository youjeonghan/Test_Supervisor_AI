from moviepy.editor import *

FILE_PATH = './video/'
SAVE_PATH = './sound/'
FILE_NAME = 'dynamite'

videoclip = VideoFileClip(FILE_PATH + FILE_NAME + '.mp4')
audioclip = videoclip.audio

audioclip.write_audiofile(SAVE_PATH + FILE_NAME + '.wav')