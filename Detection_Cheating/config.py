import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'students.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

ADMIN_ID = "Manager"
ADMIN_PW = "1234"