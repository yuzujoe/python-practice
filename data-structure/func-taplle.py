def say_something(word, *args):
    print(word)
    for arg in args:
        print(arg)

say_something("Hi", "Mike", "Nance")

t = ('MIke', "Bob")
say_something('Hi!', *t)
