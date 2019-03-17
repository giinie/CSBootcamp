a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)

x = b'mongoose'
y = x[::-1]
print(y)

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[::2])
print(a[::-2])

print(a[2::2])      #  c, e, g
print(a[-2::-2])    #  g, e, c, a
print(a[-2:2:-2])   #  g, e
print(a[2:2:-2])    #  []
