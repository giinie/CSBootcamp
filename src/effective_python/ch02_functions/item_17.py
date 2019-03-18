def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)

print('-' * 50)


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages)

print('-' * 50)

it = read_visits('my_numbers.txt')
print(list(it))
print(list(it))

print('-' * 50)


def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)

print('-' * 50)


def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result


percentages = normalize_func(lambda: read_visits('my_numbers.txt'))
print(percentages)

print('-' * 50)


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


visits = ReadVisits('my_numbers.txt')
percentages = normalize(visits)
print(percentages)

print('-' * 50)


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
print(normalize_defensive(visits))
visits = ReadVisits('my_numbers.txt')
print(normalize_defensive(visits))

print('-' * 50)

it = iter(visits)
normalize_defensive(it)
