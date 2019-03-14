def find(word):
    result = False
    while True:
        source = (yield result)
        result = word in source


f = find('Python')
next(f)

print(f.send('Hello, Python!'))
print(f.send('Hello, world!'))
print(f.send('Python Script'))

f.close()
