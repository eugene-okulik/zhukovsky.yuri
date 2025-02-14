PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_dict = {
    name: int(price[:-1])
    for item in PRICE_LIST.split('\n')
    for name, price in [item.split(' ', 1)]
}

print(new_dict)
