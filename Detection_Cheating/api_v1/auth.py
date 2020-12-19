from api_v1 import api
from flask import request
from controllers.auth_con import auth_sejong, auth_maneger

@api.route("/sejong", methods=["GET"])
def student_auth():
    data = request.get_json()
    id = data.get("id")
    pw = data.get("pw")

    return auth_sejong(id, pw)

@api.route("/manager", methods=["GET"])
def manager_auth():
    data = request.get_json()
    id = data.get("id")
    pw = data.get("pw")

    return auth_maneger(id, pw)