import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'students.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOAD_PACKET_FOLDER = "static/saves/packet/"
UPLOAD_VIDEO_FOLDER = "static/saves/video/"
UPLOAD_SOUND_FOLDER = "static/saves/sound/"
UPLOAD_WAVE_IMG_FOLDER = "static/saves/wave_img/"

ADMIN_ID = "Manager"
ADMIN_PW = "1234"