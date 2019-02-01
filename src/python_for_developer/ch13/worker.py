import pika
import time
import datetime

# 서버와 연결을 맺습니다.
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# 연결 안에서 채널을 만듭니다.
channel = connection.channel()

# [코드 13-2]와 차이점은 durable 옵션으로
# 메시지 큐 서버가 죽었다 살아 났을 때도 상태를 유지시킵니다.
channel.queue_declare(queue='task_queue', durable=True)
print(' # 메시지를 기다리고 있습니다. 종료하려면 CTRL+C를 누르세요.')

# 메시지를 처리할 콜백 함수를 지정합니다.
def callback(ch, method, properties, body):
    # 받아오는 메시지는 바이트 문자열입니다.
    # 따라서 UTF-8로 인코딩해서 msg에 저장합니다.
    msg = str(body, "utf8").split(":")

    # 몇 번째로 생성된 메시지인지 표시합니다.
    print(" # [%s] %s 메시지를 받았습니다.\n %r" % (datetime.datetime.now(), msg[0], body))

    # 받은 숫자대로 잠깐 멈춥니다.
    # 여기서는 받은 숫자를 10으로 나눠서 최대 1초만 걸리게 했습니다.
    time.sleep(int(str(msg[1]))/10)
    print(" # [%s] 완료하였습니다."% datetime.datetime.now())

    # 메시지 큐 서버에 완료했다는 응답을 보냅니다.
    # 이 응답이 가야 새로운 큐가 새로운 메시지를 보내줍니다.
    ch.basic_ack(delivery_tag = method.delivery_tag)

# 컨슈머는 메시지를 미리 가져오는데, 얼마나 가져오게 할지 결정합니다.
# 만약 이 설정이 없다면 컨슈머가 큐에 메시지를 요청할 때 무제한으로 가져옵니다.
# 또한 중간에 새로운 컨슈머를 실행하면 기존에 큐에 들어가 있던 메시지를 분배하지 않습니다.
channel.basic_qos(prefetch_count=1)

# 이 클라이언트가 수립한 채널이 어떤 큐에서 어떤 함수로 메시지를 보낼지 설정합니다.
channel.basic_consume(callback, queue='task_queue')

# 메시지 처리를 시작합니다.
channel.start_consuming()
