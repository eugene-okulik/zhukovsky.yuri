class Book:
    page_material = 'бумага'
    text_presence = False

    def __init__(self, book_title, author, number_pages, isbn, book_reservation):
        self.book_title = book_title
        self.author = author
        self.number_pages = number_pages
        self.isbn = isbn
        self.book_reservation = book_reservation


book_1 = Book('Идиот', 'Достоевский', 500, '', True)
book_2 = Book('Война и мир', 'Толстой', 1000, '', False)
book_3 = Book('Муму', 'Тургеньев', 200, '', False)
book_4 = Book('Преступление и наказание', 'Достоевский', 300, '', False)
book_5 = Book('Мастер и Маргарита', 'Булгаков', 400, '', False)

books = []
books.append(book_1)
books.append(book_2)
books.append(book_3)
books.append(book_4)
books.append(book_5)

for book in books:
    print('Название:', book.book_title + ',', 'Автор:', book.author + ',', 'страниц:',
          str(book.number_pages) + ',', 'материал:', book.page_material + ', зарезервирована'
          if book.book_reservation is True else book.page_material)


class SchoolBook(Book):

    def __init__(self, book_title, author, number_pages, isbn, book_reservation,
                 subject, school_class, task_available):
        super().__init__(book_title, author, number_pages, isbn, book_reservation)
        self.subject = subject
        self.school_class = school_class
        self.task_available = task_available


s_book_1 = SchoolBook('Алгебра', 'Иванов', 200, '', True,
                      'Математика', '9', True)
s_book_2 = SchoolBook('Всемирная история', 'Сидоров', 250, '', False,
                      'История', '6', True)
s_book_3 = SchoolBook('География Беларуси', 'Лазарев', 230, '', True,
                      'География', '10', False)

sch_books = []
sch_books.append(s_book_1)
sch_books.append(s_book_2)
sch_books.append(s_book_3)

for s_book in sch_books:
    print('Название:', s_book.book_title + ',', 'Автор:', s_book.author + ',', 'страниц:',
          str(s_book.number_pages) + ',', 'предмет:', s_book.subject + ',', 'класс:',
          s_book.school_class + ', зарезервирована' if s_book.book_reservation is True else s_book.school_class)
