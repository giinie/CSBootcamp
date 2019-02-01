# 최대공약수 구하기
# 입력: a, b
# 출력: a와 b의 최대공약수

def gcd(a, b):
    if b == 0:  # 종료 조건
        return a
    return gcd(b, a % b)  # 좀 더 작은 값으로 자기 자신을 호출

print(gcd(1, 5))    # 1
print(gcd(3, 6))    # 3
print(gcd(60, 24))  # 12
print(gcd(81, 27))  # 27

