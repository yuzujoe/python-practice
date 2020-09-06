def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result

    return wrapper

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

# 上から順番にdecoratorが実行される。
@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)
