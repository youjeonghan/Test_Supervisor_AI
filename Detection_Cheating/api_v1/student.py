from api_v1 import api
from flask import request
from flask import jsonify
from controllers.student_con import student_info, student_list_info, student_evaluat_con, submit_exam_data_con
from controllers.auth_con import auth_sejong

@api.route("/student/", methods=["GET"])
@api.route("/student/<student_id>", methods=["GET"])
def students_info(student_id = None):
    if student_id == None:
        return student_list_info(), 200
    
    else:
        return student_info(student_id), 200


@api.route("/score", methods=["POST"])
def student_evaluat():
    return student_evaluat_con(), 200


@api.route("/exam", methods=["POST"])
def submit_exam_data():
    ''' 학생 시험 데이터 제출 API '''
    id = request.form["id"]
    pw = request.form["pw"]
    if auth_sejong(id, pw)['result'] == False:
        return jsonify({
        "state": 'fail',
        "result": False
        }), 200

    return submit_exam_data_con(id), 200