import sys

sys.set_int_max_str_digits(10**6)


def fibonacci(n):
    a, b = 0, 1
    count = 1
    for _ in range(n):
        yield a
        a, b = b, a + b
        count += 1


n = 1
for a in fibonacci(100000):
    if n == 5:
        print(str(a))
    elif n == 200:
        print(a)
    elif n == 1000:
        print(a)
    elif n == 100000:
        print(str(a))
        break
    n += 1
