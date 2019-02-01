import requests
import json
from difflib import SequenceMatcher
import re

def get_kakao_video_search(q) :
    url = "https://dapi.kakao.com/v2/search/vclip"

    querystring = {"query":q}

    # 각자 발급받은 키를 입력합니다.
    header = {'authorization': 'KakaoAK <REST API 키>'}

    response = requests.request("GET", url, headers=header, params=querystring)
    result_json = json.loads(response.text)
    
    if result_json['meta']['total_count']> 0:
        kakao_videos = [{'url' : i['url'], 'thumbnail':i['thumbnail'], 'title':i['title']} for i in result_json['documents']]
    else :
        kakao_videos = []
    return kakao_videos

def get_themoviedb_info(eng_title) :
    themoviedb_url = "https://api.themoviedb.org/3/search/movie"
    p = {
        "api_key":"<API 키>",
        "query":eng_title
    }

    response = requests.get(themoviedb_url, params=p)

    # 첫 번째 결과만 가져오겠습니다.
    themoviedb_result = json.loads(response.text)
    if themoviedb_result['total_results'] > 0 :
        item = themoviedb_result['results'][0] 
    else :
        item = None
        
    return item

def get_naver_movie_info(q) : 
    url = "https://openapi.naver.com/v1/search/movie.json"

    p = {"query":q}

    headers = {
        'x-naver-client-id': "<Client ID>",
        'x-naver-client-secret': "<Client Secret>"
        }

    response = requests.get(url, headers=headers, params=p)

    naver_result = json.loads(response.text)
    items = naver_result['items']
    
    if naver_result['total'] == 0 :
        return None
    
    for i in range(len(items)):
        # 사용자가 입력한 검색어와 각 영화의 제목을 비교해서 비슷할수록 높은 점수를 매깁니다.
        items[i]['title_similarity'] = SequenceMatcher(a = q, b = items[i]['title']).ratio()
    
    # 바로 앞에서 계산한 유사도 점수가 가장 높은 항목을 돌려줍니다. 
    # 검색어와 제일 유사한 영화 제목의 정보를 돌려줍니다.
    return max(items, key= lambda x: x['title_similarity'])

def collect_movie_info(q) :
    naver_data = get_naver_movie_info(q)
    
    if naver_data is None :
        return None

    eng_title = naver_data['subtitle']

    themoviedb_data = get_themoviedb_info(q)

    # themoviedb의 검색 결과가 있으면 비슷한 영화, 추천 영화를 가져오고
    if themoviedb_data is not None :
        themoviedb_movie_id = themoviedb_data['id']
        
        p = {
            "api_key":"<API 키>"
        }
        
        similar_movie_url = "https://api.themoviedb.org/3/movie/{}/similar".format(themoviedb_movie_id)
        recommendation_url = "https://api.themoviedb.org/3/movie/{}/recommendations".format(themoviedb_movie_id)
        
        response = requests.get(similar_movie_url, data=p)
        similar_result = json.loads(response.text)['results']

        response = requests.get(recommendation_url, data=p)
        recommend_result = json.loads(response.text)['results']
    else :
        # 검색 결과가 없으면 빈 값으로 설정합니다.
        themoviedb_data = {}
        themoviedb_data['vote_average'] = naver_data['userRating']
        themoviedb_data['release_date'] = naver_data['pubDate']
        similar_result = []
        recommend_result = []
        
    kakao_data = get_kakao_video_search(q + " 영화")

    # 네이버 검색 결과의 태그 제거
    title = re.sub('<[^<]+?>', '', naver_data['title'])

    movie_info = {    
        # 다음 결과의 첫 번째 결과 정보들을 넣습니다.
        # 국내 개봉 이름
        "title":title,
        
        "poster":"https://image.tmdb.org/t/p/w500" + themoviedb_data['poster_path'],

        # 영문 제목
        "eng_title":eng_title,

        # 영화 원제
        "ogr_title":themoviedb_data['original_title'],

        # 출연 배우
        # 네이버 영화 정보에서 맨 마지막에 |가 붙어 있어서 생기는 빈 요소를 제거합니다.
        "actors" : naver_data['actor'].split("|")[:-1],
        
        # 감독
        # 네이버 영화 정보에서 맨 마지막에 |가 붙어 있어서 생기는 빈 요소를 제거합니다.
        "director" : naver_data['director'].split("|")[:-1],

        # 자세히 보러 가기 링크(네이버)
        "detail_link_naver":naver_data['link'],

        # 평점
        "rating": themoviedb_data['vote_average'],
        
        # 개봉일
        "pub_date" : themoviedb_data['release_date'],
        
        # 비슷한 영화
        "similar_movies":[item['original_title'] for item in similar_result],

        # 추천 영화
        "recommend_movies":[item['original_title'] for item in recommend_result],
        
        # 동영상 검색
        "videos" : kakao_data
    }
    
    return movie_info