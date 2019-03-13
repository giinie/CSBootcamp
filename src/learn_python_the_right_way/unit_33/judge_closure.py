def countdown(n):
    total = n + 1

    def count():
        nonlocal total
        total -= 1
        return total

    return count


n = int(input())
c = countdown(n)
for i in range(n):
    print(c(), end=' ')
