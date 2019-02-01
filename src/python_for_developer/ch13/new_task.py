import pika

# 무작위 수를 생성하는 random 모듈을 임포트합니다.
import random

# 서버와 연결을 맺습니다.
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# 연결 안에서 채널을 만듭니다.
channel = connection.channel()

# 채널 안에서 큐를 선언합니다. 새 큐를 만든다고 볼 수 있습니다.
# [코드 13-1]과 차이점은 durable 옵션으로
# 서버가 죽었다 살아 났을 때도 상태를 유지시킵니다.
channel.queue_declare(queue='task_queue', durable=True)

# 큐에 쌓아둘 메시지 리스트를 만듭니다.
# 총 100개의 메시지를 만들며 각각의 메시지는 1~10 사이의 정수입니다.
# 메시지 숫자가 곧 작업에 걸리는 시간이라고 생각해봅시다.
# 여기서 메시지의 형태는 "N:M"입니다.
# N번째로 생성되었고, 0.M초가 걸리는 작업이란 이야기입니다.
msgs = [str(i) + ":" + str(random.randrange(1, 11)) for i in range(100)]

# 메시지를 한번에 여러 개 보낼 거니까 적당히 함수 하나로 깔끔하게 묶어줍니다.
def send_msg(msg):
    channel.basic_publish(exchange='', routing_key='task_queue', body=str(msg),
        # 아까의 예제와 다른 부분입니다.
        properties=pika.BasicProperties(
            # 이 프로퍼티를 적용함으로서 메시지를 디스크에 저장해 사라지지 않게 합니다.
            # 즉, 서버가 다시 시작되어도 메시지는 살아남습니다.
            delivery_mode = 2, )
    )

# 메시지들을 큐에다 쌓아줍시다!
for msg in msgs:
    send_msg(msg)
    print(" # 메시지를 보냈습니다: %r" % msg)

# 메시지를 다 보낸 후 닫아줍니다.
connection.close()
