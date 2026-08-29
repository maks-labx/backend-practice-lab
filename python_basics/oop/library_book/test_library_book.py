import unittest

from library_book import LibraryBook


class LibraryBookTests(unittest.TestCase):
    def test_creates_book_with_title_and_author(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        self.assertEqual(book.title, "Clean Code")
        self.assertEqual(book.author, "Robert Martin")
        self.assertFalse(book.is_borrowed)
        self.assertIsNone(book.borrowed_by)
        self.assertEqual(book.borrow_count, 0)
        self.assertEqual(book.borrow_history, [])

    def test_strips_title_and_author(self):
        book = LibraryBook(" Clean Code ", " Robert Martin ")

        self.assertEqual(book.title, "Clean Code")
        self.assertEqual(book.author, "Robert Martin")

    def test_borrow_marks_book_as_borrowed(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        book.borrow("Max")

        self.assertTrue(book.is_borrowed)
        self.assertEqual(book.borrowed_by, "Max")
        self.assertEqual(book.borrow_count, 1)

    def test_borrow_adds_history_record(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        book.borrow("Max")

        self.assertEqual(
            book.borrow_history,
            [
                {
                    "action": "borrowed",
                    "user": "Max",
                }
            ],
        )

    def test_return_book_marks_book_as_available(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        book.borrow("Max")
        book.return_book()

        self.assertFalse(book.is_borrowed)
        self.assertIsNone(book.borrowed_by)

    def test_return_book_adds_history_record(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        book.borrow("Max")
        book.return_book()

        self.assertEqual(
            book.borrow_history,
            [
                {
                    "action": "borrowed",
                    "user": "Max",
                },
                {
                    "action": "returned",
                    "user": "Max",
                },
            ],
        )

    def test_book_can_be_borrowed_again_after_return(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        book.borrow("Max")
        book.return_book()
        book.borrow("Anna")

        self.assertTrue(book.is_borrowed)
        self.assertEqual(book.borrowed_by, "Anna")
        self.assertEqual(book.borrow_count, 2)

    def test_is_available_returns_true_for_not_borrowed_book(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        self.assertTrue(book.is_available())

    def test_is_available_returns_false_for_borrowed_book(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        book.borrow("Max")

        self.assertFalse(book.is_available())

    def test_get_book_info_returns_current_state(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        book.borrow("Max")

        self.assertEqual(
            book.get_book_info(),
            {
                "title": "Clean Code",
                "author": "Robert Martin",
                "is_borrowed": True,
                "borrowed_by": "Max",
                "borrow_count": 1,
            },
        )

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
            LibraryBook("   ", "Robert Martin")

        with self.assertRaises(ValueError):
            LibraryBook("Clean Code", "")

        with self.assertRaises(ValueError):
            LibraryBook("Clean Code", "   ")

    def test_title_and_author_must_be_strings(self):
        with self.assertRaises(ValueError):
            LibraryBook(None, "Robert Martin")

        with self.assertRaises(ValueError):
            LibraryBook("Clean Code", None)

    def test_user_is_required_when_borrowing(self):
        book = LibraryBook("Clean Code", "Robert Martin")

        with self.assertRaises(ValueError):
            book.borrow("")

        with self.assertRaises(ValueError):
            book.borrow("   ")

        with self.assertRaises(ValueError):
            book.borrow(None)


if __name__ == "__main__":
    unittest.main()
