import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'students.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOAD_PACKET_FOLDER = "static/packet/"
UPLOAD_VIDEO_FOLDER = "static/video/"
UPLOAD_SOUND_FOLDER = "static/sound/"

ADMIN_ID = "Manager"
ADMIN_PW = "1234"