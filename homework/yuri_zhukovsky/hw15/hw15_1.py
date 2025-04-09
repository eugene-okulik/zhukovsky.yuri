from tokenize import group

import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# -- Создайте в базе данных полный набор информации о студенте, заполнив все таблички:
# -- Создайте студента (student)

cursor.execute("INSERT INTO students (name, second_name) VALUES ('Brzegosh', 'Brzenczyshczykevich')")
student_id = cursor.lastrowid
# cursor.execute(f'SELECT * from students where id = {student_id}')
# print(cursor.fetchone())

# -- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их

insert_query_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query_books, [
        ('AQA Python', student_id),
        ('QA from A to Z', student_id)
    ]
)

# -- Создайте группу (group) и определите своего студента туда

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('Juniors AQA Python', '01_2025', '07_2025')")
group_id = cursor.lastrowid
# cursor.execute(f'SELECT * FROM `groups` where id = {group_id}')
# print(cursor.fetchone())
cursor.execute(f'UPDATE students set group_id = {group_id} WHERE id = {student_id}')

# -- Создайте несколько учебных предметов (subjects)

insert_query_subjects = "INSERT INTO subjets (title) VALUES (%s)"
cursor.executemany(
    insert_query_subjects, [
        ('Python for beginners',),
        ('SQL for beginners',)
    ]
)

cursor.execute("SELECT id FROM subjets ORDER BY id DESC LIMIT 2")
inserted_subjets_ids = cursor.fetchall()
# print(inserted_subjets_ids)

subjet2_id, subjet1_id = [row['id'] for row in inserted_subjets_ids]
# print(subjet1_id, subjet2_id)

# -- Создайте по два занятия для каждого предмета (lessons)

insert_query_lessons = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query_lessons, [
        ('Values in Python', subjet1_id),
        ('Classes in Python', subjet1_id),
        ('Selects in SQL', subjet2_id),
        ('Joins in SQL', subjet2_id)
    ]
)

cursor.execute("SELECT id FROM lessons ORDER BY id DESC LIMIT 4")
inserted_lessons_ids = cursor.fetchall()
# print(inserted_lessons_ids)

lesson4_id, lesson3_id, lesson2_id, lesson1_id = [row['id'] for row in inserted_lessons_ids]
# print(lesson4_id, lesson3_id, lesson2_id, lesson1_id)

# -- Поставьте своему студенту оценки (marks) для всех созданных вами занятий

insert_query_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query_marks, [
        (7, lesson1_id, student_id),
        (8, lesson2_id, student_id),
        (9, lesson3_id, student_id),
        (10, lesson4_id, student_id)
    ]
)

cursor.execute("SELECT id FROM marks ORDER BY id DESC LIMIT 4")
inserted_marks_ids = cursor.fetchall()
# print(inserted_marks_ids)

mark4_id, mark3_id, mark2_id, mark1_id = [row['id'] for row in inserted_marks_ids]
# print(mark4_id, mark3_id, mark2_id, mark1_id)

# -- Получите информацию из базы данных:
# -- Все оценки студента

cursor.execute(f'SELECT * from marks where student_id = {student_id}')
print("Оценки студента:", cursor.fetchall())

# -- Все книги, которые находятся у студента

cursor.execute(f'SELECT * from books where taken_by_student_id = {student_id}')
print("Книги студента:", cursor.fetchall())

# -- Для вашего студента выведите всё, что о нем есть в базе: группа, книги,
# оценки с названиями занятий и предметов (всё одним запросом с использованием Join)

# Пришлось вывовдить параметры в select_query через AS, чтобы вывести все title со всех таблиц

select_query = '''
SELECT students.name AS student_name, 
       students.second_name AS student_second_name, 
       `groups`.title AS group_title, 
       books.title AS book_title, 
       marks.value AS mark_value, 
       lessons.title AS lesson_title, 
       subjets.title AS subject_title 
FROM students
LEFT JOIN `groups` ON `groups`.id = students.group_id
LEFT JOIN books ON students.id = books.taken_by_student_id
LEFT JOIN marks ON students.id = marks.student_id
LEFT JOIN lessons ON marks.lesson_id = lessons.id
LEFT JOIN subjets ON lessons.subject_id = subjets.id
WHERE students.id = %s;
'''
cursor.execute(select_query, (student_id,))
print("Всё о студенте:", cursor.fetchall())

# Ниже сразу удаляю данные из таблиц

delete_marks_query = 'DELETE FROM marks WHERE student_id = %s'
cursor.execute(delete_marks_query, (student_id,))

delete_lessons_query = 'DELETE FROM lessons WHERE subject_id IN (%s, %s)'
cursor.execute(delete_lessons_query, (subjet1_id, subjet2_id))

delete_subjets_query = 'DELETE FROM subjets WHERE id IN (%s, %s)'
cursor.execute(delete_subjets_query, (subjet1_id, subjet2_id))

delete_groups_query = 'DELETE FROM `groups` WHERE id = %s'
cursor.execute(delete_groups_query, (group_id,))

delete_books_query = 'DELETE FROM books WHERE taken_by_student_id = %s'
cursor.execute(delete_books_query, (student_id,))

delete_students_query = 'DELETE FROM students WHERE id = %s'
cursor.execute(delete_students_query, (student_id,))

db.commit()
db.close()
