import datetime
import os

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
hw_13_data_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
my_dict = {}

with open(hw_13_data_file_path, 'r') as data_file:
    for line in data_file:
        if line:
            new_line = line.split(' - ')[0]
            key, value = new_line.split('. ', 1)
            my_dict[key] = value
print(my_dict)

for key in my_dict:
    value = my_dict[key]
    date_value = datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f")
    if key == '1':
        print('1 - it will be', date_value + datetime.timedelta(days=7), 'in a week')
    elif key == '2':
        print('2 -', date_value.strftime('%Y-%m-%d is'), date_value.strftime('%A'))
    elif key == '3':
        days_ago = str(datetime.datetime.now() - date_value).split(', ')[0]
        print('3 -', date_value.strftime('%Y-%m-%d'), 'was', days_ago, 'ago')
