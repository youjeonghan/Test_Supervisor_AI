from api import api

@api.route("/sejong", methods=["GET"])
def student_auth():
    # 학생 인증 api