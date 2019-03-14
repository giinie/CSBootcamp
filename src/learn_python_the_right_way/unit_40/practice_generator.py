def file_read():
    with open('words.txt') as file:
        line = None
        while line != '':
            line = file.readline()
            yield line.strip('\n')


for i in file_read():
    print(i)
