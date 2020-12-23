'''
analysis controller
'''
from flask import current_app
from models import db, Students
from datetime import datetime
import scapy.all as sc

def getPacketTime(packet_path):
    try:
        pkts = sc.rdpcap(packet_path)
    except MemoryError:
        print("Memory Error로 인해 packet을 열지 못하였습니다.")
        return None

    pktTimes = []
    pktTime = datetime.fromtimestamp(pkts[0].time)
    pktTimes.append(pktTime.strftime("%Y-%m-%d %H:%M:%S"))

    pktTime = datetime.fromtimestamp(pkts[len(pkts) - 1].time)
    pktTimes.append(pktTime.strftime("%Y-%m-%d %H:%M:%S"))

    return pktTimes

def network_analysis_con(student):
    '''네트워크 분석
    Args:
        student: Students객체

    Returns:
        return: 사용한 패킷 목록 리스트 (String)
    '''

    # pcapng = current_app.config["UPLOAD_PACKET_FOLDER"] + f"{student.student_number}.pcapng"

    result = []
    with open(student.packet_path, "rb") as f:
        string = f.read().hex()
        if "676f6f676c6561647365727669636573" in string: #google search(googleadservices)
            result.append("Google")
        if "7365617263682e6e617665722e" or "626c6f672e6e61766572" in string: #search.naver, blog.naver
            result.append("Naver")
        if "7365617263682e6461756d2e" in string: #search.daum
            result.append("Daum")
        if "6b616b616f" in string: #kakao
            result.append("KaKaoTalk")
        if "646973636f7264" in string: #discord
            result.append("Discord")
        if "796f7574756265" in string: #youtube
            result.append("Youtube")
        if "676974687562" in string: #github
            result.append("Github")

    list = str()
    for i, packet in enumerate(result):
        if len(result)-1 == i:
            list = list + packet 
        else:
            list = list + packet + "/"
    
    student = Students.query.filter(Students.student_number == student.student_number)
    student.update({'network_result': list})
    # student = student.first()

    temp_range = getPacketTime(student.first().packet_path)
    

    time_range = temp_range[0] + "/" +temp_range[1]
    student.update({'time_range': time_range})

    db.session.commit()
