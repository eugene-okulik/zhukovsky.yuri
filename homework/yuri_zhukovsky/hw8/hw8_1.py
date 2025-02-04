import random

salary = input('Введите сумму: ')
random_boolean = random.choice([True, False])
if random_boolean:
    print((str(salary) + ','), ''.join(str(random_boolean)),
          str('- \'$' + str(int(salary) + (int(random.random() * random.choice([100, 1000, 10000])))) + '\''))
else:
    print((str(salary) + ','), ''.join(str(random_boolean)), str('- \'$' + str(int(salary)) + '\''))
