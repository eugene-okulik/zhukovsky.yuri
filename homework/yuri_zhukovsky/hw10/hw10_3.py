first = int(input('Введите first: '))
second = int(input('Введите second: '))


def repeat_me(func):

    def wrapper(first, second):
        operation = ''
        if first == second:
            operation = '+'
        elif first < 0 or second < 0 and first != second:
            operation = '*'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        else:
            operation = None

        if operation:
            return func(first, second, operation)
        else:
            return "Некорректная операция"

    return wrapper


@repeat_me
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


result = calc(first, second)
print("Результат:", result)
