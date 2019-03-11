input_list = list(map(int, input().split(';')))

input_list.sort(reverse=True)

print(input_list)

for i in input_list:
    print('{:>9,}'.format(i))
