names = ['Cecilia', 'Lisa', 'Maria']
letters = [len(name) for name in names]
# print(names)
# print(letters)

longest_name = None
max_letters = 0

# for i in range(len(names)):
#     count = letters[i]
#     if count > max_letters:
#         longest_name = names[i]
#         max_letters = count
#
# print(longest_name)
#
# for i, name in enumerate(names):
#     count = letters[i]
#     if count > max_letters:
#         longest_name = name
#         max_letters = count
#
# print(longest_name)
#
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

# print(longest_name)

names.append('Rosalind')
for name, count in zip(names, letters):
    print(name)

from itertools import zip_longest

# names.append('Rosalind')
for name, count in zip_longest(names, letters):
    print(name)
