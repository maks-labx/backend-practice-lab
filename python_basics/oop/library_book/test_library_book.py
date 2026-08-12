import unittest

from library_book import LibraryBook


class LibraryBookTests(unittest.TestCase):
    def test_creates_book_with_title_and_author(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        self.assertEqual(book.title, "Clean Code")
        self.assertEqual(book.author, "Robert Martin")
        self.assertFalse(book.is_borrowed)
        self.assertIsNone(book.borrowed_by)

    def test_borrow_marks_book_as_borrowed(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        book.borrow("Max")

        self.assertTrue(book.is_borrowed)
        self.assertEqual(book.borrowed_by, "Max")

    def test_return_book_marks_book_as_available(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        book.borrow("Max")
        book.return_book()

        self.assertFalse(book.is_borrowed)
        self.assertIsNone(book.borrowed_by)

    def test_is_available_returns_true_for_not_borrowed_book(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        self.assertTrue(book.is_available())

    def test_is_available_returns_false_for_borrowed_book(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        book.borrow("Max")

        self.assertFalse(book.is_available())

    def test_cannot_borrow_already_borrowed_book(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        book.borrow("Max")

        with self.assertRaises(ValueError):
            book.borrow("Anna")

    def test_cannot_return_book_that_is_not_borrowed(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        with self.assertRaises(ValueError):
            book.return_book()

    def test_title_and_author_are_required(self):
        with self.assertRaises(ValueError):
            LibraryBook("", "Robert Martin")

        with self.assertRaises(ValueError):
            LibraryBook("Clean Code", "")


if __name__ == "__main__":
    unittest.main()
