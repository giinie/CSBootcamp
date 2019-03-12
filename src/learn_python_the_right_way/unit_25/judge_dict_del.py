keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

x = {k: v for k, v in x.items() if k != 'delta' and v != 30}

print(x)
