import select
from threading import Thread
from time import time


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


numbers = [2139079, 1214759, 1516637, 1852285]


# start = time()
# for number in numbers:
#     list(factorize(number))
# end = time()
# print('Took %.3f seconds' % (end - start))
# print('-' * 50)


class FactorizeThread(Thread):
    def __init__(self, number):
        super(FactorizeThread, self).__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


start = time()
threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
end = time()
print('Took %.3f seconds' % (end - start))


def slow_systemcall():
    select.select([], [], [], 0.1)


start = time()
for _ in range(5):
    slow_systemcall()
end = time()
print('Took %.3f seconds' % (end - start))

start = time()
threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)


def compute_helicopter_location(index):
    pass


for i in range(5):
    compute_helicopter_location(i)
for thread in threads:
    thread.join()
end = time()
print('Took %.3f seconds' % (end - start))
