a = [[10, 20], [30, 40], [50, 60]]

for i in a:
    for j in i:
        print(j, end=' ')
    print()

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

i = 0
while i < len(a):
    x, y = a[i]
    print(x, y)
    i += 1

i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end=' ')
        j += 1
    print()
    i += 1

a = []
for i in range(3):
    line = []
    for j in range(2):
        line.append(0)
    a.append(line)
print(a)

print([[0 for j in range(2)] for i in range(3)])

print([[0] * i for i in [3, 1, 3, 2, 5]])

students = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]]
print(sorted(students, key=lambda student: student[1]))
print(sorted(students, key=lambda student: student[2]))
