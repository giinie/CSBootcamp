y = [10, 20, 30]

try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    z = y[index] / x
except ZeroDivisionError as e:  # as 뒤에 변수를 지정하면 에러를 받아옴.
    print('숫자를 0으로 나눌 수 없습니다.', e)  # e 에 저장된 에러 메시지 출력
except IndexError as e:
    print('잘못된 인덱스입니다.', e)
except Exception as e:  # 모든 예외의 에러 메시지를 출력할 때는 Exception 을 사용.
    print('예외가 발생했습니다.', e)
else:  # try 코드에서 예외가 발생하지 않았을 때 실행됨.
    print(z)
