# from random import randint
#
# random_bits = 0
# for i in range(64):
#     if randint(0, 1):
#         random_bits |= 1 << i
#     print(random_bits)

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print('%s is delicious' % flavor)

for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('{}: {}'.format(i + 1, flavor))

# enumerate
for i, flavor in enumerate(flavor_list):
    print('{}: {}'.format(i + 1, flavor))

for i, flavor in enumerate(flavor_list, 1):
    print('{}: {}'.format(i, flavor))
