# double-ended queue
from collections import deque

fifo = deque()
fifo.append(1)      # producer
fifo.append(2)
fifo.append(3)
x = fifo.popleft()  # consumer
print(x)
print(fifo.pop())
print('-' * 50)

a = {}
a['foo'] = 1
a['bar'] = 2

from random import randint

# Randomly populate 'b' to cause hash conflicts
# while True:
#     z = randint(99, 1013)
#     b = {}
#     for i in range(z):
#         b[i] = i
#     b['foo'] = 1
#     b['bar'] = 2
#     for i in range(z):
#         del b[i]
#     if str(b) != str(a):
#         break
#
# print(a)
# print(b)
# print('Equal?', a == b)
# print('-' * 50)

# ordered dict
from collections import OrderedDict
a = OrderedDict()
a['foo'] = 1
a['bar'] = 2

b = OrderedDict()
b['foo'] = 'red'
b['bar'] = 'blue'

for value1, value2 in zip(a.values(), b.values()):
    print(value1, value2)
print('-' * 50)

# default dict
stats = {}
key = 'my_counter'
if key not in stats:
    stats[key] = 0
stats[key] += 1
print(stats)

from collections import defaultdict
stats = defaultdict(int)
stats['my_counter'] += 1
print(dict(stats))
print('-' * 50)

# heap queue : priority queue
from heapq import *
a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)

print(heappop(a), heappop(a), heappop(a), heappop(a))

a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)
print(a[0])
print(nsmallest(1, a)[0])
print(nsmallest(2, a))

print('Before:', a)
a.sort()
print('After:', a)

# bi section
x = list(range(10**6))
i = x.index(991234)
print(i)

from bisect import bisect_left
i = bisect_left(x, 991234)
print(i)

from timeit import timeit
print(timeit(
    'a.index(len(a)-1)',
    'a = list(range(100))',
    number=1000))
print(timeit(
    'bisect_left(a, len(a)-1)',
    'from bisect import bisect_left;'
    'a = list(range(10**6))',
    number=1000))
