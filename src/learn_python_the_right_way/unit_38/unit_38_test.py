# try:
#     x = int(input('나눌 숫자를 입력하세요: '))
#     y = 10 / x
#     print(y)
# except:  # 예외가 발생했을 때 실행됨.
#     print('예외가 발생했습니다.')

x = int(input('3의 배수를 입력하세요: '))
assert x % 3 == 0, '3의 배수가 아닙니다.'
print(x)
