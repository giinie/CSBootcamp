# 최댓값 구하기
# 입력: 숫자가 n개 들어 있는 리스트
# 출력: 숫자 n개 중 최댓값

def find_max(a, n):  # 리스트 a의 앞부분 n개 중 최댓값을 구하는 재귀 함수
    if n == 1:
        return a[0]
    max_n_1 = find_max(a, n - 1) # n-1개 중 최댓값을 구함
    if max_n_1 > a[n - 1]:       # n-1개 중 최댓값과 n-1번 위치 값을 비교
        return max_n_1
    else:
        return a[n - 1]

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v, len(v)))  # 함수에 리스트의 자료 갯수를 인자로 추가하여 호출
