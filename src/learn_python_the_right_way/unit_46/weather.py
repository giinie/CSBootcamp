import requests                 # 웹 페이지의 html 을 가져오는 모듈
from bs4 import BeautifulSoup   # html 을 파싱하는 모듈

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦.
response = requests.get('https://pythondojang.bitbucket.io/weather/observation/currentweather.html')
soup = BeautifulSoup(response.content, 'html.parser')

# <table class="table_develop3">을 찾음
table = soup.find('table', {'class': 'table_develop3'})
data = []                           # 데이터를 저장할 리스트 생성
for tr in table.find_all('tr'):     # 모든 <tr> 태그를 찾아서 반복. 각 지점의 데이터를 가져옴
    tds = list(tr.find_all('td'))   # 모든 <td> 태그를 찾아서 반복. 각 날씨 값을 리스트로 만듦.
    for td in tds:                  # <td> 태그 리스트 반복(각 날씨 값을 가져옴)
        if td.find('a'):            # <td> 안에 <a> 태그가 있으면(지점인지 확인)
            point = td.find('a').text   # <a> 태그 안에서 지점을 가져옴
            temperature = tds[5].text   # <td> 태그 리스트의 여섯 번째(인덱스 5)에서 기온을 가져옴
            humidity = tds[9].text      # <td> 태그 리스트의 열 번째(인덱스 9)에서 습도를 가져옴
            data.append([point, temperature, humidity])  # data list 에 지점, 기온, 습도를 추가

# print(data)
with open('weather.csv', 'w') as file:
    file.write('point,temperature,humidity\n')
    for i in data:
        file.write('{},{},{}\n'.format(i[0], i[1], i[2]))

# csv 파일을 읽어서 DataFrame 객체 생성. 인덱스 컬럼은 point로 설정
df = pd.read_csv('weather.csv', index_col='point')
# print(df)
# 특별시, 광역시만 모아서 DataFrame 객체 생성
city_df = df.loc[['서울', '인천', '대전', '대구', '광주', '부산', '울산']]
# print(city_df)
mpl.rc('font', family='d2coding')

ax = city_df.plot(kind='bar', title='날씨', figsize=(12, 4), legend=True, fontsize=12)
ax.set_xlabel('도시', fontsize=12)
ax.set_ylabel('기온/습도', fontsize=12)
ax.legend(['기온', '습도'], fontsize=12)
# plt.show()

print(city_df['temperature'])
print(city_df.humidity)
print(city_df.temperature.idxmax())
print(city_df.temperature.idxmin())
print(city_df.loc[city_df.temperature.idxmax()])
print(city_df.loc[city_df.temperature.idxmin()])
