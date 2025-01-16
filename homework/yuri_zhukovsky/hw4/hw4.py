my_dict = {'tuple': (1, 'BMW', 3, True, 5),
           'list': ['BLR', 20, 3.13, 4, '50'],
           'dict': {'ip': '1.1.1.1', 'port': 245, 'name': 'Marina', 'brand': 'Zara', 'flag': False},
           'set': {None, 'text', False, 2.42, 3}}

print('\nTask_1')
y_tuple = my_dict['tuple']
print('Last element is', y_tuple[-1])

print('\nTask_2')
y_list = my_dict['list']
y_list.append('ytest')
y_list.pop(1)
print(y_list)

print('\nTask_3')
y_dict = my_dict['dict']
y_dict['i am a tuple'] = 6
y_dict.pop('port')
print(y_dict)

print('\nTask_4')
y_set = my_dict['set']
y_set.add(10)
y_set.remove(None)
print(y_set)

print('\nDictionary:')
print(my_dict)
