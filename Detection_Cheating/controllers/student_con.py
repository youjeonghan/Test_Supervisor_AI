'''
student controller
'''
import os
from flask import jsonify
from flask import current_app
from flask import request
from models import Students
from models import db

def student_info(st_number):
    student = Students.query.filter(Students.student_number == st_number).first()

    return jsonify({
        "state": 'success',
        "result": student.serialize
    })


def student_list_info():
    studentlist = Students.query.all()
    returnlist = []
    for i, student in enumerate(studentlist):
        returnlist.append(dict())
        returnlist[i].update(result=student.serialize)
        returnlist[i].update(state="success")

    return jsonify(returnlist)


def student_evaluat_con():
    student = Students.query.filter(Students.student_number == st_number).first()
    result = False
    if student.state == "pass":
        result = True

    return jsonify({
        "state": 'success',
        "result": result
    })


def submit_exam_data_con(id):
    pcapng = request.files["pcapng"]
    mp4 = request.files["mp4"]

    pcapng.save(os.path.join(current_app.config["UPLOAD_PACKET_FOLDER"], f"{id}.pcapng"))
    mp4.save(os.path.join(current_app.config["UPLOAD_VIDEO_FOLDER"], f"{id}.mp4"))
    
    return jsonify({
        "state": 'success',
        "result": True
    })