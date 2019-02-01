'''
# bot이 반응할 수 있게하는 디코레이터 함수들을 임포트합니다.
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.dispatcher import Message

# 무엇에 반응할지 잡아줄 수 있는 re(정규식) 패키지를 임포트합니다.
import re

# listen_to는 채널에서 오가는 모든 대화에 반응합니다.
# 디코레이터 함수의 첫 번째 파라미터는 정규식이고 두 번째 파라미터는 플래그입니다.
@listen_to("Hello", re.IGNORECASE)

# 첫 번째 파라미터는 디스패처의 메시지 클래스입니다.
# 반응해야 할 채널에 메시지를 보내는 함수등이 있습니다.
# 여기 없는 두 번째 이후의 파라미터는 위 정규식에 그룹이 있을 경우 매칭된 문자열이 들어갑니다.
# 개수는 상한이 없습니다. 그룹 숫자에 따라 파라미터를 더 늘리면 됩니다.
def hello(msg: Message):
    # send는 채널에 그냥 말합니다.
    msg.send("World!!")

# respond_to는, @을 이용해서 멘션했을 경우에만 반응합니다. 나머지는 listen_to의 역할과 같습니다.
@respond_to("hi", re.IGNORECASE)
def hi(msg: Message):
    # reply는 해당 반응을 일으킨 사람에게 말합니다.
    # listen_to든 respond_to든 말을 건 사람에게 대답합니다.
    msg.reply("Thank you 39!!")
'''

# 무작위 숫자를 생성하기 위한 random 모듈을 임포트합니다.
import random

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.dispatcher import Message
import re

# 'roll 던지는횟수d숫자면체' 형식으로 메시지를 입력하는 hello() 함수를 정의합니다.
@listen_to("roll (\d*)d(\d+)", re.IGNORECASE)

# 메시지, 주사위를 던지는 횟수, 주사위의 면체를 지정하는 파라미터를 넣어줍니다.
def hello(msg: Message, number_of_die: str, side_of_die: str):
    #
    roll_result = [random.randrange(1, int(side_of_die), 1) for i in range(int(number_of_die))]

    # 주사위를 던진 횟수만큼 나온 숫자를 모두 더합니다.
    roll_sum = sum(roll_result)

    # 주사위를 던져서 나온 숫자와 합을 메시지로 출력합니다.
    msg.send(str(roll_result))
    msg.send(str(roll_sum))
