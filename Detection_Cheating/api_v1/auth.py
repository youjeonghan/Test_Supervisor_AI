from api_v1 import api
from flask import request
from flask import jsonify
from controllers.auth_con import auth_sejong, auth_maneger

@api.route("/sejong", methods=["POST"])
def student_auth():
    data = request.get_json()
    id = data.get("id")
    pw = data.get("pw")

    print(id)
    print(pw)

    return jsonify(auth_sejong(id, pw))

@api.route("/manager", methods=["POST"])
def manager_auth():
    data = request.get_json()
    id = data.get("id")
    pw = data.get("pw")

    return auth_maneger(id, pw)