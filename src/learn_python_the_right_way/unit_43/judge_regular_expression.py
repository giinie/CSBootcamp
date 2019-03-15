import re

p = re.compile('^http://|https://[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+(/[a-zA-Z0-9-_.?=])*$')

url = input()

print(p.match(url) != None)
