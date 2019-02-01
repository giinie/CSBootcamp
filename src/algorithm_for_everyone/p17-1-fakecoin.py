# 주어진 동전 n개 중에 가짜 동전(fake)을 찾아내는 알고리즘
# 입력: 전체 동전 위치의 시작과 끝(0, n - 1)
# 출력: 가짜 동전의 위치 번호

# 무게 재기 함수
# a에서 b까지 놓인 동전과
# c에서 d까지 놓인 동전의 무게를 비교
# a에서 b까지에 가짜 동전이 있으면(가벼우면): -1
# c에서 d까지에 가짜 동전이 있으면(가벼우면): 1
# 가짜 동전이 없으면(양쪽 무게가 같으면): 0
def weigh(a, b, c, d):
    fake = 29  # 가짜 동전의 위치(알고리즘은 weigh 함수를 이용하여 이 값을 맞혀야 함)
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0

# weigh 함수(저울질)를 이용하여
# left와 right까지에 있는 가짜 동전의 위치를 찾아냄
def find_fakecoin(left, right):
    for i in range(left + 1, right + 1):  # left+1부터 right까지 반복
        # 가장 왼쪽 동전과 나머지 동전을 차례로 비교
        result = weigh(left, left, i, i)
        if result == -1:   # left 동전이 가벼움(left 동전이 가짜)
            return left
        elif result == 1:  # i 동전이 가벼움(i 동전이 가짜)
            return i
        # 두 동전의 무게가 같으면 다음 동전으로

    # 모든 동전의 무게가 같으면 가짜 동전이 없는 예외 경우
    return -1

n = 100    # 전체 동전 개수
print(find_fakecoin(0, n - 1))
