'''
student controller
'''
import os
from flask import jsonify
from flask import current_app
from flask import request
from models import Students
from models import db, Students
from controllers.auth_con import auth_sejong

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
    data = request.get_json()
    student_number = data.get("student_number")
    pass = data.get("pass")
    reason = data.get("reason")

    student = Students.query.filter(Students.student_number == student_number).first()

    db.session.commit()

    if pass == True:

    return jsonify({
        "state": 'success',
        "result": pass
    })


def submit_exam_data_con(student_number):
    pcapng = request.files["pcapng"]
    mp4 = request.files["mp4"]

    pcapng.save(os.path.join(current_app.config["UPLOAD_PACKET_FOLDER"], f"{student_number}.pcapng"))
    mp4.save(os.path.join(current_app.config["UPLOAD_VIDEO_FOLDER"], f"{student_number}.mp4"))

    Students.query.filter(Students.student_number == student_number).first().update({
        'packet_path': current_app.config["UPLOAD_PACKET_FOLDER"] + f"{student_number}.pcapng", 
        'video_path': current_app.config["UPLOAD_VIDEO_FOLDER"] + f"{student_number}.mp4"
        })
    
    return jsonify({
        "state": 'success',
        "result": True
    })

def student_create(student_number):
    student = Students()
    student.student_number = student_number
    student.name = auth_sejong(student_number, pw)['name']

    db.session.add(student)
    db.session.commit()
    
    return student