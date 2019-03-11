col, row = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(row):
    for j in range(col):
        if matrix[i][j] == '.':
            fk = i - 1
            tk = i + 2
            if fk < 0:
                fk = 0
            if tk >= row:
                tk = row
            fl = j - 1
            tl = j + 2
            if fl < 0:
                fl = 0
            if tl >= col:
                tl = col
            matrix[i][j] = [matrix[k][l] for k in range(fk, tk) for l in range(fl, tl)].count('*')

print()
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end='')
    print()
