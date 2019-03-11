a, b = map(int, input().split())

print([2 ** i for i in range(a, b + 1) if i != a + 1 and i != b - 1])
