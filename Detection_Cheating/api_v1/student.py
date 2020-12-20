from api_v1 import api
from flask import request
from controllers.student_con import student_info, student_list_info

@api.route("/student/", methods=["GET"])
@api.route("/student/<student_id>", methods=["GET"])
def students_info(student_id = None):
    if student_id == None:
        return student_list_info(), 200
    
    else:
        return student_info(student_id), 200