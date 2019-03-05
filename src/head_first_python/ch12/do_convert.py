import pprint
from datetime import datetime


def convert2ampm(time24: str) -> str:
    """24시간 형식으로 제공된 문자열 시간을 AM/PM 형식의 문자열로 변환."""
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint.pprint(flights)
print()

flights2 = {}
for k, v in flights.items():
    flights2[convert2ampm(k)] = v.title()

pprint.pprint(flights2)

fts = {convert2ampm(k): v.title() for k, v in flights.items()}

pprint.pprint(fts)
print()

when = {}
for dest in set(flights2.values()):
    when[dest] = [k for k, v in flights2.items() if v == dest]

pprint.pprint(when)

when2 = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}

pprint.pprint(when2)
print()
