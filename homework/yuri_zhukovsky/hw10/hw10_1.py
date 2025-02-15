def finish_me(func):

    def wrapper(*text):
        func(*text)
        print('finished')

    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')
