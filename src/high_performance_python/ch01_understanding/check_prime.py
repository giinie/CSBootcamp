import math


def check_prime(number):
    sqrt_number = math.sqrt(number)
    number_float = float(number)
    for i in range(2, int(sqrt_number) + 1):
        if (number_float / i).is_integer():
            return False
    return True


def better_check_prime(number):
    sqrt_number = math.sqrt(number)
    number_float = float(number)
    numbers = range(2, int(sqrt_number) + 1)
    for i in range(2, len(numbers), 5):
        # 아래 코드는 유효한 파이썬 코드가 아니다.
        result = (number_float / numbers[i:(i+5)]).is_integer()
        if any(result):
            return False
    return True


def check_prime_mine(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


print('check_prime(10000000) = ', check_prime(10000000))
print('check_prime(10000019) = ', check_prime(10000019))
print('check_prime_mine(10000000) = ', check_prime_mine(10000000))
print('check_prime_mine(10000019) = ', check_prime_mine(10000019))
