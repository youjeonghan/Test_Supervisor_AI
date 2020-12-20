from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Students(db.Model):
    '''학생 정보와 결과'''
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    student_number = db.Column(db.Integer)
    name = db.Column(db.String(10))
    video_path = db.Column(db.String(30))
    audio_path = db.Column(db.String(30))
    audio_img_path = db.Column(db.String(10))
    state = db.Column(db.String(10))
    reason = db.Column(db.Text())
    network_result = db.Column(db.String(200))
    audio_result = db.Column(db.String(500))
    # eye_result = db.Column(db.String(100))
    