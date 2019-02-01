# 앞서 만든 영화 정보를 모으는 함수를 임포트합니다
from movie_search import collect_movie_info
from flask import Flask
from flask import request
from flask import render_template
import json

app = Flask(__name__)

app.debug = True

# 결과를 json으로 저장합니다.
@app.route("/movie-search")
def search():
    q = request.args.get("q")
    return json.dumps(collect_movie_info(q),ensure_ascii=False).encode('utf8')

# 결과를 html 페이지로 보여줍니다.
@app.route("/movie-search-pretty")
def search_pretty():
    q = request.args.get("q")
    result = collect_movie_info(q)
    return render_template('result.html',item = result)

if __name__ == "__main__":
    app.run()