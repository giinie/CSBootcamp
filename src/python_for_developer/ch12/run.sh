#!/bin/bash

# cron의 경우 실행되는 PATH가 다릅니다.
# 따라서 사용자의 PATH 변수로 크론을 실행할 경로를 설정해줍니다.
PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

# 가상 환경을 설정했다면, 가상 환경을 활성화하는 셸 스크립트도 들어가야 합니다.
source <absolute-path-to-venv>/bin/activate
python3 <absolute-path-to-script>/slack_timer_bot.py
