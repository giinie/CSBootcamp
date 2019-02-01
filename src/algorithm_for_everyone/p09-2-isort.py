# 삽입 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)

def ins_sort(a):
    n = len(a)
    for i in range(1, n):  # 1부터 n-1까지
        # i번 위치의 값을 key로 저장
        key = a[i]
        # j를 i 바로 왼쪽 위치로 저장
        j = i - 1
        # 리스트의 j번 위치에 있는 값과 key를 비교해 key가 삽입될 적절한 위치를 찾음
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]  # 삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            j -= 1
        a[j + 1] = key  # 찾은 삽입 위치에 key를 저장

d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)
