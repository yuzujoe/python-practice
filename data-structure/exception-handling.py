l = [1, 2, 3]
i = 5

try:
    l[i]
except IndexError as ex:
    print("Don't worry {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}'.format(ex))
else:
    print('done')
finally:
    print('clean up')


class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as ex:
    print('This is my fault. Go Next')