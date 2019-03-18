def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)

print('-' * 50)


def sort_priority2(numbers, group):
    found = False

    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found


found = sort_priority2(numbers, group)
print('Found:', found)
print(numbers)

print('-' * 50)


def sort_priority3(numbers, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found


found = sort_priority3(numbers, group)
print('Found:', found)
print(numbers)

print('-' * 50)


class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)


sorter = Sorter(group)
numbers.sort(key=sorter)
print('Found:', sorter.found)
print(numbers)

print('-' * 50)

