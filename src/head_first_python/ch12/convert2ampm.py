from datetime import datetime


def convert2ampm(time24: str) -> str:
    """24시간 형식으로 제공된 문자열 시간을 AM/PM 형식의 문자열로 변환."""
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')
