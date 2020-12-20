'''
student controller
'''
from flask import jsonify
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
    if student.state == pass
        result = True

    return jsonify({
        "state": 'success',
        "result": result
    })


def submit_exam_data_con():
    id = request.form.get("id")
    pw = request.form.get("pw")
    uploaded_files = request.files.get("file")
    uploaded_files = request.files.get("file")