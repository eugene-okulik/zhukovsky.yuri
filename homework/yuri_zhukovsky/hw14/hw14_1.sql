-- Создайте в базе данных полный набор информации о студенте, заполнив все таблички:
-- Создайте студента (student)

INSERT INTO students (name, second_name) VALUES ('Brzegosh', 'Brzenczyshczykevich')

SELECT * from students where id = 4899

-- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их

INSERT INTO books (title, taken_by_student_id) VALUES ('AQA Python', 4899)

INSERT INTO books (title, taken_by_student_id) VALUES ('QA from A to Z', 4899)

SELECT * from books where id in (40, 41)

-- Создайте группу (group) и определите своего студента туда

INSERT INTO `groups` (title, start_date, end_date) VALUES ('Juniors AQA Python', '01_2025', '07_2025')

SELECT * FROM `groups` where id = 4865

UPDATE students set group_id = 4865 WHERE id = 4899

-- Создайте несколько учебных предметов (subjects)

INSERT INTO subjets (title) VALUES ('Python for beginers')

INSERT INTO subjets (title) VALUES ('SQL for beginers')

SELECT * FROM subjets where id in (5158, 5159)

-- Создайте по два занятия для каждого предмета (lessons)

INSERT INTO lessons (title, subject_id) VALUES ('Values in Python', 5158)

INSERT INTO lessons (title, subject_id) VALUES ('Classes in Python', 5158)

INSERT INTO lessons (title, subject_id) VALUES ('Selects in SQL', 5159)

INSERT INTO lessons (title, subject_id) VALUES ('Joins in SQL', 5159)

SELECT * from lessons where id in (9335, 9336, 9337, 9338)

-- Поставьте своему студенту оценки (marks) для всех созданных вами занятий

INSERT INTO marks (value, lesson_id, student_id) VALUES (7, 9335, 4899)

INSERT INTO marks (value, lesson_id, student_id) VALUES (8, 9336, 4899)

INSERT INTO marks (value, lesson_id, student_id) VALUES (9, 9337, 4899)

INSERT INTO marks (value, lesson_id, student_id) VALUES (10, 9338, 4899)

SELECT * from marks where id in (7608, 7609, 7610, 7611) order by id ASC

-- Получите информацию из базы данных:
-- Все оценки студента

SELECT * from marks where student_id = 4899

-- Все книги, которые находятся у студента

SELECT * from books where taken_by_student_id = 4899

-- Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов (всё одним запросом с использованием Join)

SELECT s.name, s.second_name, g.title, b.title, m.value, l.title, s2.title FROM students s
JOIN `groups` g on g.id = s.group_id
JOIN books b on s.id = b.taken_by_student_id 
JOIN marks m on s.id = m.student_id
JOIN lessons l on m.lesson_id = l.id
JOIN subjets s2 on l.subject_id = s2.id
where s.id = 4899

