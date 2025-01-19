# Task 1
print('Task 1')
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# Task 2
print('\nTask 2')
ro_1 = 'результат операции: 42'
ro_2 = 'результат операции: 514'
rrp = 'результат работы программы: 9'
iro_1 = ro_1.index(':') + 2
iro_2 = ro_2.index(':') + 2
irrp = rrp.index(':') + 2
print(int(ro_1[iro_1:]) + 10)
print(int(ro_2[iro_2:]) + 10)
print(int(rrp[irrp:]) + 10)

# Task 3
print('\nTask 3')
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
