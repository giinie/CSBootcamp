# pika를 임포트합니다.
import pika

# 서버와 연결을 맺습니다.
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# 연결 안에서 채널을 만듭니다.
channel = connection.channel()

# 채널 안에서 큐를 선언합니다. 새 큐를 만든다고 할 수 있습니다.
channel.queue_declare(queue='hello')

# 메시지를 보냅니다. 여기서는 교환기excahnge와 routing_key를 다루지 않을 겁니다.
# channel.basic_publish(exchange='', routing_key='hello', body='Hello Miku!!!')
# print("# 메시지를 보냈습니다!")
for i in range(10000):
    # 10,000개의 메시지를 큐에 쌓습니다.
    channel.basic_publish(exchange='', routing_key='hello', body=str(i))
    print("# 메시지를 보냈습니다!" + str(i))

# 서버와의 연결을 끊습니다.
connection.close()
