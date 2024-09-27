import os

os.system ('cls')

l = [4, 1, 3, 2]

l.insert(0, 100)
print(l)

l.remove(100)
print(l)

l.sort()
print(l)

l.reverse()
print(l)

l.pop(0)
print(l)

l.append(0)
print(l)

print(l.index(3))