from api_v1 import api
from flask import request
from flask import jsonify
from flask import current_app
from controllers.student_con import student_info, student_list_info, student_evaluat_con
from controllers.student_con import submit_exam_data_con, student_create
from controllers.auth_con import auth_sejong
from controllers.analysis_con import network_analysis_con
from controllers.catch_voice_con import catchVoiceTimeZone
from controllers.sound_save_con import sound_save

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
    ''' 학생 시험 데이터 제출 API 
    requests: form
        id: 세종 Portal ID
        pw: 세종 Portal PW
        pcapng: pcapng 파일
        mp4: 영상 파일
    '''
    student_number = request.form["id"]
    pw = request.form["pw"]
    if auth_sejong(student_number, pw)['result'] == False:
        return jsonify({
        "state": 'fail',
        "result": False
        }), 200
    
    ### 학생 데이터 생성 / 학번, 이름 입력 ###
    ### id / student_number / name ###
    student = student_create(student_number, pw)

    ### 패킷, 영상 파일 저장 ###
    ### packet_path / video_path ###
    submit_exam_data_con(student_number)

    ### 네트워크 분석 ###
    ### network_result / video_path ###
    network_analysis_con(student)

    ### 음성 저장 ###
    sound_save(student_number)

    ### 음성 분석 ###
    ### audio_path / audio_messages ###
    catchVoiceTimeZone(current_app.config["UPLOAD_SOUND_FOLDER"], student_number+".wav", student)

    ### 음성 파형 이미지 분석 ###
    

    # 지원이 코드 삽입 (wav, 목소리 출력 리스트)
    

    return jsonify(), 200