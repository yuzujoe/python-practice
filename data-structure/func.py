def say_something():
    s = "hi"
    return s

result = say_something()
print(result)

def what_is_this(color):
    if color == "red":
        return 'tomato'
    elif color == 'green':
        return 'green papper'
    else:
        return "I don't know"

result = what_is_this('green')
print(result)

def add_num(a: int, b: int):
    return a + b
# stringを入れてもエラーにならない
r = add_num(10, 20)
print(r)

def menu(entree, drink, dessert):
    print('entree =', entree)
    print('drink = ', drink)
    print('dessert =', dessert)

menu(entree="beef", dessert="ice", drink="beer")

# pythonはデフォルト引数を与えるべきではない
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func(100)
print(r)

r = test_func(100)
print(r)
