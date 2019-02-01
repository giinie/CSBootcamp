# 최대공약수 구하기
# 입력: a, b
# 출력: a와 b의 최대공약수

def gcd(a, b):
    i = min(a, b) # 두 수 중에서 최솟값을 구하는 파이썬 함수
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1  # i를 1만큼 감소시킴

print(gcd(1, 5))    # 1
print(gcd(3, 6))    # 3
print(gcd(60, 24))  # 12
print(gcd(81, 27))  # 27
