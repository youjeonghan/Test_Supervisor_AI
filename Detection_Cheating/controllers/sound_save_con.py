from moviepy.editor import *
from flask import current_app
from models import db, Students

# FILE_PATH = './video/'
# SAVE_PATH = './sound/'
FILE_NAME = 'dynamite'
VIDEO_EXTENSION = 'mp4'
AUDIO_EXTENSION = 'wav'
def sound_save(student_number, student):
    # videoclip = VideoFileClip(current_app.config["UPLOAD_VIDEO_FOLDER"] + student_number + '.' + VIDEO_EXTENSION)
    videoclip = VideoFileClip(student.video_path)
    audioclip = videoclip.audio

    temp = str()
    temp = current_app.config["UPLOAD_SOUND_FOLDER"]
    temp = temp + f"{student_number}.wav"

    student = Students.query.filter(Students.student_number == student.student_number)
    student = student.update({
        'audio_path': temp
        })
    db.session.commit()

    # videoclip.write_videofile(SAVE_PATH + FILE_NAME)
    audioclip.write_audiofile(current_app.config["UPLOAD_SOUND_FOLDER"] + student_number + '.' + AUDIO_EXTENSION)