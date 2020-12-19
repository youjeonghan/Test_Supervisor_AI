from moviepy.editor import *

FILE_PATH = './video/'
SAVE_PATH = './sound/'
FILE_NAME = 'dynamite'
VIDEO_EXTENSION = 'mp4'
AUDIO_EXTENSION = 'wav'

videoclip = VideoFileClip(FILE_PATH + FILE_NAME + '.' + VIDEO_EXTENSION)
audioclip = videoclip.audio

# videoclip.write_videofile(SAVE_PATH + FILE_NAME)
audioclip.write_audiofile(SAVE_PATH + FILE_NAME + '.' + AUDIO_EXTENSION)