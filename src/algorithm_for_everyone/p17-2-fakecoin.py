# 주어진 동전 n개 중에 가짜 동전(fake)을 찾아내는 알고리즘
# 입력: 전체 동전 위치의 시작과 끝(0, n - 1)
# 출력: 가짜 동전의 위치 번호

# 무게 재기 함수
# a에서 b까지에 놓인 동전과
# c에서 d까지에 놓인 동전의 무게를 비교
# a에서 b까지에 가짜 동전이 있으면(가벼우면): -1
# c에서 d까지에 가짜 동전이 있으면(가벼우면): 1
# 가짜 동전이 없으면(양쪽 무게가 같으면): 0
def weigh(a, b, c, d):
    fake = 29  # 가짜 동전의 위치(알고리즘은 weigh() 함수를 이용하여 이 값을 맞혀야 함)
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0

# weigh() 함수(저울질)를 이용하여
# left와 right까지에 놓인 가짜 동전의 위치를 찾아냄
def find_fakecoin(left, right):
    # 종료 조건 : 가짜 동전이 있을 범위 안에 동전이 한 개뿐이면 그 동전이 가짜 동전임
    if left == right:
        return left
    # left와 right까지에 놓인 동전을 두 그룹(g1_left~g1_right, g2_left~g2_right)으로 나눔
    # 동전 수가 홀수면 두 그룹으로 나누고 한 개가 남음
    half = (right - left + 1) // 2
    g1_left = left
    g1_right = left + half - 1
    g2_left = left + half
    g2_right = g2_left + half - 1
    # 나눠진 두 그룹을 weigh() 함수를 이용하여 저울질함
    result = weigh(g1_left, g1_right, g2_left, g2_right)
    if result == -1:  # 그룹 1이 가벼움(가짜 동전이 이 그룹에 있음)
        return find_fakecoin(g1_left, g1_right)  # 그룹 1 범위를 재귀 호출로 다시 조사
    elif result == 1:  # 그룹 2가 가벼움(가짜 동전이 이 그룹에 있음)
        return find_fakecoin(g2_left, g2_right)  # 그룹 2 범위를 재귀 호출로 다시 조사
    else:  # 두 그룹의 무게가 같으면(나뉜 두 그룹 안에 가짜 동전이 없다면)
        return right  # 두 그룹으로 나뉘지 않고 남은 나머지 한 개의 동전이 가짜

n = 100    # 전체 동전 개수
print(find_fakecoin(0, n - 1))
