import os
import csv
import dotenv
import mysql.connector as mysql

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
hw_16_data_csv_file = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

print(hw_16_data_csv_file)

csv_data = []
with open(hw_16_data_csv_file, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    data = []
    for row in file_data:
        # print(row)
        csv_data.append(row)

# print(csv_data)

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

select_query = '''
SELECT students.name AS name,
students.second_name AS second_name,
`groups`.title AS group_title,
books.title AS book_title,
subjets.title AS subject_title,
lessons.title AS lesson_title,
marks.value AS mark_value
FROM students
LEFT JOIN `groups` ON `groups`.id = students.group_id
LEFT JOIN books ON students.id = books.taken_by_student_id
LEFT JOIN marks ON students.id = marks.student_id
LEFT JOIN lessons ON marks.lesson_id = lessons.id
LEFT JOIN subjets ON lessons.subject_id = subjets.id;
'''
cursor.execute(select_query)
db_data = cursor.fetchall()
# print(cursor.fetchall())

# Преобразуем данные из БД в удобный формат для сравнения
db_records = {(
    d['name'],
    d['second_name'],
    d['group_title'],
    d['book_title'],
    d['subject_title'],
    d['lesson_title'],
    d['mark_value']) for d in db_data}

# Сравнение данных из CSV с данными из БД
missing_records = []
for row in csv_data:
    csv_record = tuple(row)  # Преобразуем строку из CSV в кортеж для сравнения
    if csv_record not in db_records:
        missing_records.append(csv_record)

# Выводим записи, которых нет в БД
print("Записи, которых нет в БД:")
for record in missing_records:
    print(record)

db.commit()
db.close()
