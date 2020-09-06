def counter(num=10):
    for _ in range(num):
        yield 'run'

def greeting():
    yield 'Good Morning'
    yield 'Good Afternoon'
    yield 'Good night'

g = greeting()
c = counter()

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print('###############')

print(next(g))
print(next(c))
print(next(c))
print(next(c))

print('################')

print(next(g))


def g():
    for i in range(10):
        yield i

# tupleにしたい場合は tuple()とする。
g = (i for i in range(10))
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
