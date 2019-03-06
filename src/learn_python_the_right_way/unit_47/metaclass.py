def replace(self, old, new):
    while old in self:
        self[self.index(old)] = new


AdvancedList = type('AdvancedList', (list, ), {'desc': '향상된 리스트', 'replace': replace})

x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)

print(x)
print(x.desc)


class MakeCalc(type):
    def __new__(mcs, name, bases, namespace):
        namespace['desc'] = '계산 클래스'
        namespace['add'] = lambda self, a, b: a + b
        return type.__new__(mcs, name, bases, namespace)


Calc = MakeCalc('Calc', (), {})
c = Calc()
print(c.desc)
print(c.add(1, 2))


