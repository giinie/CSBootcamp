# n명에서 두 명을 뽑아 짝을 만드는 모든 경우를 찾는 알고리즘
# 입력: n명의 이름이 들어 있는 리스트
# 출력: 두 명을 뽑아 만들 수 있는 모든 짝

def print_pairs(a):
    n = len(a)  # 리스트의 자료 개수를 n에 저장
    for i in range(0, n - 1):      # 0부터 n-2까지 반복
        for j in range(i + 1, n):  # i+1부터 n-1까지 반복
            print(a[i], "-", a[j])

name = ["Tom", "Jerry", "Mike"]
print_pairs(name)
print()
name2 = ["Tom", "Jerry", "Mike", "John"]
print_pairs(name2)
