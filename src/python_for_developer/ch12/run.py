# slackbot 패키지의 Bot 클래스를 불러옵니다.
from slackbot.bot import Bot

# Bot 클래스 객체를 생성하고 실행합니다.
def main():
    bot = Bot()
    bot.run()

# 이 스크립트에서 실행할 것을 작성합니다. 앞에서 만든 main을 실행하게 만들었습니다.
if __name__ == "__main__":
    main()
