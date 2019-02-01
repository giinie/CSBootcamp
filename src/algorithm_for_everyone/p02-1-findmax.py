# 최댓값 구하기
# 입력: 숫자가 n개 들어 있는 리스트
# 출력: 숫자 n개 중 최댓값

def find_max(a):
    n = len(a)    # 입력 크기 n
    max_v = a[0]  # 리스트의 첫 번째 값을 최댓값으로 기억
    for i in range(1, n):  # 1부터 n-1까지 반복
        if a[i] > max_v:   # 이번 값이 현재까지 기억된 최댓값보다 크면
            max_v = a[i]   # 최댓값을 변경
    return max_v

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v))
