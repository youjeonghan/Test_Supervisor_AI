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
from datetime import datetime

def student_info(st_number):
    student = Students.query.filter(Students.student_number == st_number).first()

    returndict = {}

    temp = []
    temp2 = []
    temp3 = []

    returndict = student.serialize

    temp = student.network_result.split('/')
    returndict['network_result'] = temp

    ###
    temp = student.audio_messages.split('/')
    returndict['audio_messages'] = temp

    temp = student.audio_result.split(',')
    for t in temp:
        temp2 = t.split('-')
        temp3.append(temp2)

    returndict['audio_result'] = temp3

    ### eye_ratio
    eye_ratio = {
        "left": student.eye_ratio_left,
        "right": student.eye_ratio_right,
        "center": student.eye_ratio_center,
        "blink": student.eye_ratio_blink
    }
    returndict['eye_ratio'] = eye_ratio

    ### time_range
    time_range = student.time_range.split('/')
    returndict['time_range'] = time_range

    return jsonify({
        "state": 'success',
        "result": returndict
    })


def student_list_info():
    studentlist = Students.query.all()
    returnlist = []
    for i, student in enumerate(studentlist):
        returnlist.append(dict())
        
        
        # returnlist[i].update(result=student.serialize)
        returnlist[i] = student.serialize
        
        temp = []
        temp2 = []
        temp3 = []

        temp = student.network_result.split('/')
        # returnlist[i]['result']['network_result'] = temp
        returnlist[i]['network_result'] = temp

        temp = student.audio_result.split(',')
        for t in temp:
            temp2 = t.split('-')
            temp3.append(temp2)

        # returnlist[i]['result']['audio_result'] = temp3
        returnlist[i]['audio_result'] = temp3

        ### eye_ratio
        eye_ratio = {
            "left": student.eye_ratio_left,
            "right": student.eye_ratio_right,
            "center": student.eye_ratio_center,
            "blink": student.eye_ratio_blink
        }
        returnlist[i]['eye_ratio'] = eye_ratio

        ### time_range
        time_range = student.time_range.split('/')
        returnlist[i]['time_range'] = time_range


    return jsonify({
        "state": 'success',
        "result": returnlist
    })


def student_evaluat_con():
    data = request.get_json()
    student_number = data.get("student_number")
    pass_ = data.get("pass")
    reason = data.get("reason")

    student = Students.query.filter(Students.student_number == student_number).first()
    student.state = pass_
    student.reason = reason
    db.session.commit()

    return jsonify({
        "state": 'success',
        "result": pass_
        })


def submit_exam_data_con(student_number):
    pcapng = request.files["pcapng"]
    mp4 = request.files["mp4"]

    # 저장할 이름을 정함 (suffix를 통해 중복 구분)
    suffix = datetime.now().strftime("%y%m%d_%H%M%S")
    pcapng_save_name = student_number + f"_{suffix}.pcapng"
    mp4_save_name = student_number + f"_{suffix}.mp4"

    pcapng.save(os.path.join(current_app.config["UPLOAD_PACKET_FOLDER"], pcapng_save_name))
    mp4.save(os.path.join(current_app.config["UPLOAD_VIDEO_FOLDER"], mp4_save_name))

    

    Students.query.filter(Students.student_number == student_number).update({
        'packet_path': current_app.config["UPLOAD_PACKET_FOLDER"] + pcapng_save_name,
        'video_path': current_app.config["UPLOAD_VIDEO_FOLDER"] + mp4_save_name
        })
    db.session.commit()

    return jsonify({
        "state": 'success',
        "result": True
    })

def student_create(student_number, pw):
    student = Students.query.filter(Students.student_number == student_number).first()
    if student == None:
        student = Students()
        student.student_number = student_number
        student.name = auth_sejong(student_number, pw)['name']

        db.session.add(student)
        db.session.commit()
    
    return student