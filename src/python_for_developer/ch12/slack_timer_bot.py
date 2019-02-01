# requests 패키지를 임포트합니다.
import requests

# 날짜와 시간을 다루는 datetime 패키지를 임포트합니다.
import datetime

def main():
    url = "<웹훅 URL 입력>"

    # 보낼 메시지를 설정합니다. 여기서는 datetime.datetime.now()를 이용해 시간을 표시합니다.
    text = "테스트 메시지입니다: " + str(datetime.datetime.now())

    # 보낼 메시지의 JSON 문자열 형태를 설정합니다.
    payload = {
        "text": text
    }

    # POST로 요청을 보냅니다.
    requests.post(url, json=payload)

# 이 스크립트에서 실행할 것을 작성합니다. 앞에서 만든 main()을 실행하게 만들었습니다.
if __name__ == "__main__":
    main()
