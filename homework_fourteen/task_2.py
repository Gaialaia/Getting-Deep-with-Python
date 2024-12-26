# Задача 2. Тестирование класса с использованием unittest
# Напишите класс Library, который управляет книгами. Класс должен поддерживать
# следующие методы:
# ●add_book(title): добавляет книгу в библиотеку.
# ●remove_book(title): удаляет книгу из библиотеки.
# ●list_books(): возвращает список всех книг в библиотеке.
# При попытке удалить книгу, которая не существует, должно выб
import unittest


class BookNotFoundError(Exception):
    pass


class Library:

    library = []

    def __init__(self):
        self.library = list()

    def add_book(self, title):
        self.library.append(title)

    def remove_book(self, title):
        if title not in self.library:
            raise BookNotFoundError('The book is not found')
        self.library.remove(title)

    #
    # def list_books(self):
    #     for book in self.library:
    #         print(book)

    def list_books(self):
        return list(self.library)

    def __str__(self):
        return f'{self.library}'


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book('The power of the actor')
        self.assertIn('The power of the actor', self.library.list_books())

    def test_remove_book(self):
        self.library.add_book('The power of the actor')
        self.library.remove_book('The power of the actor')
        self.assertNotIn('The power of the actor', {self.library})

    def test_list_books(self):
        return self.library

    def test_remove_exc_book(self):
        with self.assertRaises(BookNotFoundError):
            self.library.remove_book('The book')


if __name__ == '__main__':

    lib = Library()
    lib.add_book('Gone with the wind')
    lib.add_book('Народные сказки')
    lib.remove_book('Gone with the wind')
    lib.add_book('Python Crash Course')
    # l.remove_book('Beach')
    lib.add_book('Atlas Shrugged')
    lib.add_book('The Fountainhead')
    lib.list_books()
    unittest.main()
