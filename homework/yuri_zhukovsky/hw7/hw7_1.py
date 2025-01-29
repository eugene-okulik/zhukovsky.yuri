a = 10
user_input = input('Угадайте число: ')
while int(user_input) != a:
    print('Попробуйте снова ...')
    user_input = input('Угадайте число: ')
print('Поздравляю! Вы угадали!')
