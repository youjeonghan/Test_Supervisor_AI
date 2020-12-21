"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
import sys

def GazeYourEye(video):
    gaze = GazeTracking()
    webcam = cv2.VideoCapture(video)
    result = []
    while True:
        # We get a new frame from the webcam
        value, frame = webcam.read()
        # We send this frame to GazeTracking to analyze it
        if value==False: break
        gaze.refresh(frame)

        frame = gaze.annotated_frame()
        #text = ""

        if gaze.is_blinking():
            #text = "Blinking"
            result.append('B')
        elif gaze.is_right():
            #text = "Looking right"
            result.append('R')
        elif gaze.is_left():
            #text = "Looking left"
            result.append('L')
        elif gaze.is_center():
            #text = "Looking center"
            result.append('C')

        # cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

        # left_pupil = gaze.pupil_left_coords()
        # right_pupil = gaze.pupil_right_coords()
        # cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        # cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

        # cv2.imshow("analysis", frame)

        if cv2.waitKey(1) == 27:
            break
    whole = len(result)
    ret = [round(result.count('C')/whole*100,2),round(result.count('B')/whole*100,2),round(result.count('L')/whole*100,2),round(result.count('R')/whole*100,2)]
    if ret[0]>=94: #center 비율이 94 넘으면 P
        return "P",ret
    else: return "NP",ret