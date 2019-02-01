# 연속한 숫자의 곱을 구하는 알고리즘
# 입력: n
# 출력: 1부터 n까지 연속한 숫자를 곱한 값

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

print(fact(1))   # 1! = 1
print(fact(5))   # 5! = 120
print(fact(10))  # 10! = 3628800

