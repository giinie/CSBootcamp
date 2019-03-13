class AdvancedList(list):
    def replace(self, old, new):
        # for i in range(len(self)):
        #     if self[i] == old:
        #         self[i] = new
        # return self
        while old in self:
            self[self.index(old)] = new


x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)
