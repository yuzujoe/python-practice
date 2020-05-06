d = {'x': 10, 'y': 20}

print(d['x'], d['y'])

d['z'] = 100
print(d)

print(d.keys())
print(d.values())

d2 = {'x': 1000, 'j': 500}
print(d2)
d.update(d2)
print(d)

d.pop('x')
print(d)

d.clear()
print(d)

x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)
