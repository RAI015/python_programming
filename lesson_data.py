class UppdercaseError(Exception):
    pass


def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppdercaseError(word)


try:
    check()
except UppdercaseError as ex:
    print('This is my fault. Go next')

