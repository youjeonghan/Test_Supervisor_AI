'''
auth controller
'''
import requests
from flask import jsonify
from bs4 import BeautifulSoup as bs
import getpass

header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\
            AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
            "Accept":"text/html,application/xhtml+xml,application/xml;\
            q=0.9,imgwebp,*/*;q=0.8"}
do_url = "https://do.sejong.ac.kr/ko/process/member/login"
TIMEOUT_SEC = 3

def sjlms_api(id, pw):
    data = {"username":id, "password":pw, "rememberusername":"1"}
    with requests.Session() as s:
        page = s.post("http://sjulms.moodler.kr/login/index.php", 
            headers = header, data = data, timeout=TIMEOUT_SEC)
        soup = bs(page.text, "html.parser")
        if soup.find("h4") is None:
            return {"result":False}
        else:
            name = soup.find("h4").get_text()
            major = soup.find("p",{"class":"department"}).get_text()
            return {
            "result":True,
            "name":name,
            "id":id,
            "major":major
            }

def dosejong_api(id, pw):
    data = {
            #POST
            "email":id,
            "password":pw
            }
    with requests.Session() as s:
        html = s.post(do_url, headers = header, data = data, timeout=TIMEOUT_SEC).content
        html = s.get("https://do.sejong.ac.kr/", timeout=TIMEOUT_SEC).text
        soup = bs(html, "html.parser")
        soup = soup.select("div.info")
        if soup == []: return {"result": False}
        name = soup[0].find("b").get_text().strip()
        major = soup[0].find("small").get_text().strip().split(" ")[1]
        return {
            "result":True,
            "name":name,
            "id":id,
            "major":major
        }

def uis_api(id, pw):
    uis_header = {
    "Referer": "https://portal.sejong.ac.kr",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
    }
    LOGIN_INFO = {
        'id': id,
        'password': pw,
        'rtUrl': '',
    }
    with requests.Session() as s:
        login_req = s.post('https://portal.sejong.ac.kr/jsp/login/login_action.jsp', 
            headers=uis_header, data=LOGIN_INFO, timeout=TIMEOUT_SEC)
        res = s.get('http://uis.sejong.ac.kr/app/sys.Login.servj', timeout=TIMEOUT_SEC)
        res = s.get('http://uis.sejong.ac.kr/app/menu/sys.MenuSys.doj', timeout=TIMEOUT_SEC)
        soup = bs(res.content, 'html.parser')
        name = soup.select_one('form[name="MainForm"] table tr td strong')
        if name is None: return {"result":False}
        name = name.get_text().replace(" ", "").replace("님", "").replace("\n", "").replace("\r","")
        return {
            "result":True,
            "name":name,
            "id":id,
            "major":"none"
        }

def auth_sejong(id, pw):
    '''학생 인증
    Args:
        id: 학교아이디
        pw: 비밀번호

    Returns:
        True or False
    '''
    print(dosejong_api(id,pw))
    print(sjlms_api(id,pw))
    print(uis_api(id, pw))
    result = False
    if dosejong_api(id,pw)['result'] == True:
        result = True

    elif sjlms_api(id,pw)['result'] == True:
        result = True

    elif uis_api(id,pw)['result'] == True:
        result = True

    return {
        "state": 'success',
        "result": result
    }

def auth_maneger(id, pw):
    '''관리자 인증
    Args:
        id: 관리자아이디
        pw: 비밀번호

    Returns:
        True or False
    '''
    result = False
    if id =="Manager" and pw =="1234":
        result = True

    return jsonify({
        "state": 'success',
        "result": result
    })