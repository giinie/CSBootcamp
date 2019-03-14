try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:                              # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아닙니다.')  # 예외를 발생시킴.
    print(x)
except Exception as e:  # 모든 예외의 에러 메시지를 출력할 때는 Exception 을 사용.
    print('예외가 발생했습니다.', e)
finally:  # 예외 발생 여부과 상관없이 항상 실행됨.
    print('코드 실행이 끝났습니다.')
