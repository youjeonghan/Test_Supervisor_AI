from api_v1 import api
from flask import request
from flask import jsonify
from controllers.analysis_con import network_analysis_con

@api.route("/network/<student_id>", methods=["POST"])
def network_analysis(student_id):
    return jsonify(network_analysis_con(student_id))