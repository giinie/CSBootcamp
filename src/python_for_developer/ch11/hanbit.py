# -*- coding: utf-8 -*-
# 플라스크를 임포트합니다.
from flask import Flask

# 플라스크에서 request 객체를 사용하도록 임포트합니다.
from flask import request

# JSON 라이브러리를 임포트합니다.
import json

# SQLite3 라이브러리를 임포트합니다.
import sqlite3

# 플라스크 앱을 생성합니다.
app = Flask(__name__)

# 편의를 위한 디버그 모드를 활성화합니다.
app.debug = True

# 데이터베이스에 연결하는 함수를 정의합니다.
def get_db_con() -> sqlite3.connect:
    return sqlite3.connect("db.sqlite")

# URL 경로에 따라 실행할 함수에 디코레이터를 사용합니다. 디코레이터의 파라미터는 URL 경로입니다.
@app.route("/")

# 모든 데이터를 내려받기 위한 hello() 함수를 정의합니다.
def hello():
    # con이라는 변수를 생성해 데이터베이스에 접속합니다.
    with get_db_con() as con:
        # 커서를 가져옵니다.
        cur = con.cursor()

        # hanbit_books 데이터베이스의 모든 데이터를 선택합니다.
        q = "select * from hanbit_books"
        result = cur.execute(q)

    # 결과를 JSON 문자열로 만들어줍니다.
    result_json = jsonize(result)

    # 결과를 돌려줍니다.
    return result_json

# 저자 이름 요청을 받을 url을 정해줍니다.
@app.route("/books/by/author")

# 해당 url을 받아서 저자 이름을 가져올 함수를 선언합니다.
def get_books_by_author():
    # 파라미터에서 name을 받아옵니다.
    name = request.args.get("name")

    # 데이터베이스 커넥션을 가져와서 작업합니다.
    # 작업이 끝나면 자동으로 with가 close를 호출합니다.
    with get_db_con() as con:
        cur = con.cursor()

        # 쿼리를 작성합니다. hanbit_books 테이블에서 author 컬럼이
        # name과 일치하는 걸 찾아옵니다.
        q = "SELECT * FROM hanbit_books WHERE author LIKE :name ORDER BY title"
        param = {
            "name": "%" + name + "%"
        }

        result = cur.execute(q, param)

    result_json = jsonize(result)

    return result_json

# 출간월 요청을 받을 url을 정해줍니다.
@app.route("/books/by/month")

# 해당 url을 받아서 출간월을 가져올 함수를 선언합니다.
def get_books_by_month():
    # 파라미터에서 month를 받아옵니다.
    month = request.args.get("month")

    # 숫자가 한 자리일 경우 앞에 "0"을 붙여줍니다.
    if int(month) < 10:
        month = "0" + month

    with get_db_con() as con:
        cur = con.cursor()

        # 쿼리를 작성합니다. hanbit_books 테이블에서 pub_date 컬럼의
        # 월 부분이 month와 일치하는걸 찾아옵니다.
        q = "SELECT * FROM hanbit_books WHERE strftime('%m', pub_date) = :month ORDER BY pub_date DESC"
        param = {
            "month": month
        }

        result = cur.execute(q, param)

    result_json = jsonize(result)

    return result_json

# 데이터베이스 커서의 result를 받아서 JSON 문자열로 만드는 함수입니다.
def jsonize(result):
    result_json = json.dumps(list(result.fetchall()), ensure_ascii=False).encode("utf-8")
    return result_json

# 이 파일을 바로 실행할 때 함께 실행할 코드를 적습니다.
if __name__ == "__main__":
    # 위에서 생성한 플라스크 애플리케이션을 실행합니다.
    app.run()
