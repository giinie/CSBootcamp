value = [len(x) for x in open('item_08.py', 'r')]
print(value)

it = (len(x) for x in open('item_08.py', 'r'))
print(it)

# for item in it:
#     print(item)

roots = ((x, x**0.5) for x in it)

for item in roots:
    print(item)
