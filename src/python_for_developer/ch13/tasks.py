# 셀러리를 임포트합니다.
from celery import Celery

# 샐러리 앱 인스턴스를 만듭니다.
app = Celery(
    # 첫 번째 파라미터는 현재 모듈의 이름입니다.
    # 이 파라미터를 전달하면 현재 모듈을 단독으로 실행할 때도 문제 없도록 합니다.
    'tasks',

    # broker 파라미터는 메시지 브로커의 주소입니다. 프로토콜과 접속 정보를 적습니다.
    # 여기서는 rabbitmq를 사용하므로, AMQP 형식의 주소를 사용했습니다.
    broker='pyamqp://guest@localhost//',

    # 결과를 저장할 backend를 지정합니다. 주로 데이터베이스를 지정합니다.
    backend="db+sqlite:///db.sqlite"
)

# @app.task 디코레이터를 붙여 이 함수가 태스크라는 것을 표시합니다.
@app.task
def add(x, y):
    return x + y
