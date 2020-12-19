def whatis(pcapng):
    result = []
    with open(pcapng,"rb") as f:
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
            
    return result
