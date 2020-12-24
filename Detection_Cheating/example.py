"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
from models import db, Students
import numpy as np
import joblib

global load_model
load_model = joblib.load('model.pkl')

def GazeYourEye(video, student):
    gaze = GazeTracking()
    webcam = cv2.VideoCapture(video)
    result = []
    while True:
        value, frame = webcam.read()
        if value==False: break
        gaze.refresh(frame)

        frame = gaze.annotated_frame()

        if gaze.is_blinking():
            result.append('B')
        elif gaze.is_right():
            result.append('R')
        elif gaze.is_left():
            result.append('L')
        elif gaze.is_center():
            result.append('C')


        if cv2.waitKey(1) == 27:
            break
    whole = len(result)

    ret = [round(result.count('C')/whole*100,2),round(result.count('B')/whole*100,2),round(result.count('L')/whole*100,2),round(result.count('R')/whole*100,2)]
    

    student = Students.query.filter(Students.student_number == student.student_number)
    student.update({
        'eye_ratio_center': ret[0],
        'eye_ratio_blink': ret[1],
        'eye_ratio_left': ret[2],
        'eye_ratio_right': ret[3]
    })
    

    data = np.array([[ret[0], ret[1], ret[2], ret[3]]])
    [result] = load_model.predict(data)
    student.update({'eye_result': bool(result) })
    db.session.commit()

