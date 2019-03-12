with open('words_27_6.txt', 'r') as file:
    words = file.readline().split()

for word in words:
    if 'c' in word:
        print(word.strip(',.'))
