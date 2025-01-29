ro_1 = 'результат операции: 42'
ro_2 = 'результат операции: 54'
rrp = 'результат работы программы: 209'
rez = 'результат: 2'


def process_res(*results):
    values = []

    for result in results:
        value = int(result.split(': ')[1])
        values.append(value)

    for value in values:
        print(value + 10)


process_res(ro_1, ro_2, rrp, rez)
