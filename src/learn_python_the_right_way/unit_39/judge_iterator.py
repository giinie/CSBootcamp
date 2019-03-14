class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     if self.start < self.stop:
    #         current = self.start
    #         mm, ss = divmod(current, 60)
    #         hh, mm = divmod(mm, 60)
    #         hh = hh % 24
    #         self.start += 1
    #         return '{:02d}:{:02d}:{:02d}'.format(hh, mm, ss)
    #     else:
    #         raise StopIteration

    def __getitem__(self, item):
        if self.start + item < self.stop:
            current = self.start + item
            mm, ss = divmod(current, 60)
            hh, mm = divmod(mm, 60)
            hh = hh % 24
            # self.start += 1  # 주의필요
            return '{:02d}:{:02d}:{:02d}'.format(hh, mm, ss)
        else:
            raise IndexError


start, stop, index = map(int, input().split())
for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')
