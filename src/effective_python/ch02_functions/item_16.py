from itertools import islice


def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


address = 'Four score and seven years ago...'
result = index_words(address)
print(result[:3])

print('-' * 50)


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


result = list(index_words_iter(address))
print(result[:3])

print('-' * 50)


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


with open('address.txt', 'r') as f:
    it = index_file(f)
    result = islice(it, 0, 3)
    print(list(result))

print('-' * 50)

