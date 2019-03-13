class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(str_time):
        h, m, s = map(int, str_time.split(':'))
        return h <= 24 and m <= 59 and s <= 60

    @classmethod
    def from_string(cls, str_time):
        return cls(*str_time.split(':'))


time_string = input()
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')
