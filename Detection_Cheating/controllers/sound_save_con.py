from moviepy.editor import *
from flask import current_app

# FILE_PATH = './video/'
# SAVE_PATH = './sound/'
FILE_NAME = 'dynamite'
VIDEO_EXTENSION = 'mp4'
AUDIO_EXTENSION = 'wav'
def sound_save(student_number):
    videoclip = VideoFileClip(current_app.config["UPLOAD_VIDEO_FOLDER"] + student_number + '.' + VIDEO_EXTENSION)
    audioclip = videoclip.audio

    # videoclip.write_videofile(SAVE_PATH + FILE_NAME)
    audioclip.write_audiofile(current_app.config["UPLOAD_SOUND_FOLDER"] + student_number + '.' + AUDIO_EXTENSION)