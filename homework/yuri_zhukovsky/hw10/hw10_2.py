def repeat_me(func):

    def wrapper(text, count):
        i = 1
        while i <= count:
            func(text)
            i += 1

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)


# Второй вариант сделал с помощью AI; разобрался, как работает


def repeat_me(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
