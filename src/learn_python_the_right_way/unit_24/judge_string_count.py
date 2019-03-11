import string

str_list = input().split()

for index, value in enumerate(str_list):
    str_list[index] = value.strip(string.punctuation)

print(str_list.count('the'))
