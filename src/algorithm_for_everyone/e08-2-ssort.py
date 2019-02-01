# 내림차순 선택 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)

def sel_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        max_idx = i  # 최솟값(min) 대신 최댓값(max)을 찾아야 함
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:  # 부등호 방향 뒤집기
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]

d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)
