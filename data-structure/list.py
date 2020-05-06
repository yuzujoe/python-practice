s = ['a,' 'b', 'c', 'd', 'e', 'g']
print(s[0])

s[0] = 'x'
print(s)

print(s[2:5])
s[2:5] = ['C', 'D', 'E']
print(s)

s[2:5] = []
print(s)

s[:] = []
print(s)

n = [1, 2, 3, 4, 5, 6, 7, 8]
n.append(100)
print(n)

n.insert(0, 200)
print(n)

n.pop()
print(n)

n.pop(0)
print(n)

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))
print(r.count(3))

if 100 in r:
    print('exsits')

r.sort()
print(r)

r.reverse()
print(r)

s = 'My name is Mike.'
to_split = s.split(' ')
print(s)

x = ' '.join(to_split)
print(x)

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =', j)
print('i =', i)

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('y =', y)
print('x =', x)
