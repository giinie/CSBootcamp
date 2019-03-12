# word = input('단어를 입력하세요: ')
#
# is_palindrome = True
# for i in range(len(word) // 2):
#     if word[i] != word[-1 - i]:
#         is_palindrome = False
#         break
#
# is_palindrome_mine = word == word[::-1]
#
# print(is_palindrome)
# print('my_way :', is_palindrome_mine)

# text = 'Hello'
#
# for i in range(len(text) - 1):
#     print(text[i], text[i + 1], sep='')
#     print('my way :', text[i:i+2])

# text = 'this is python script'
# words = text.split()
#
# for i in range(len(words) - 1):
#     print(' '.join(words[i:i+2]))

text = 'hello'

two_gram = zip(text, text[1:])
for i in two_gram:
    print(i[0], i[1], sep='')
