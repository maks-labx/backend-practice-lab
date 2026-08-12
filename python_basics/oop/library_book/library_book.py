class LibraryBook:
    def __init__(self, title, author):
        if not title:
            raise ValueError("Title is required")

        if not author:
            raise ValueError("Author is required")

        self.title = title
        self.author = author
        self.is_borrowed = False
        self.borrowed_by = None

    def borrow(self, user):
        if not user:
            raise ValueError("User is required")

        if self.is_borrowed:
            raise ValueError("Book is already borrowed")

        self.is_borrowed = True
        self.borrowed_by = user

    def return_book(self):
        if not self.is_borrowed:
            raise ValueError("Book is not borrowed")

        self.is_borrowed = False
        self.borrowed_by = None

    def is_available(self):
        return not self.is_borrowed
