# 리스트에서 특정 숫자 위치 찾기
# 입력: 리스트 a, 찾는 값 x 
# 출력: 찾으면 그 값의 위치, 찾지 못하면 -1

def search_list(a, x):
    n = len(a)  # 입력 크기 n
    for i in range(0, n):  # 리스트 a의 모든 값을 차례로
        if x == a[i]:      # x 값과 비교하여
            return i       # 같으면 위치 돌려줍니다.

    return -1   # 끝까지 비교해서 없으면 -1을 돌려줍니다.

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))   # 2(순서상 세 번째지만, 위치 번호는 2)
print(search_list(v, 33))   # 3(33은 리스트에 두 번 나오지만 처음 나온 위치만 출력)
print(search_list(v, 900))  # -1(900은 리스트에 없음)

