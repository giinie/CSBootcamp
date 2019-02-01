# 연속한 숫자의 곱을 구하는 알고리즘
# 입력: n
# 출력: 1부터 n까지 연속한 숫자를 곱한 값

def fact(n):
    f = 1                      # 곱을 계산할 변수, 초깃값은 1
    for i in range(1, n + 1):  # 1부터 n까지 반복(n+1은 제외)
        f = f * i              # 곱셈 연산으로 수정
    return f

print(fact(1))   # 1! = 1
print(fact(5))   # 5! = 120
print(fact(10))  # 10! = 3628800
