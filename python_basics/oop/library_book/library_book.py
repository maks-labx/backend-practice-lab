class LibraryBook:
    def __init__(self, title, author):
        self.title = self._validate_required_text(title, "Title")
        self.author = self._validate_required_text(author, "Author")
        self.is_borrowed = False
        self.borrowed_by = None
        self.borrow_count = 0
        self.borrow_history = []

    def borrow(self, user):
        user = self._validate_required_text(user, "User")

        if self.is_borrowed:
            raise ValueError("Book is already borrowed")

        self.is_borrowed = True
        self.borrowed_by = user
        self.borrow_count += 1
        self.borrow_history.append(
            {
                "action": "borrowed",
                "user": user,
            }
        )

    def return_book(self):
        if not self.is_borrowed:
            raise ValueError("Book is not borrowed")

        user = self.borrowed_by

        self.is_borrowed = False
        self.borrowed_by = None
        self.borrow_history.append(
            {
                "action": "returned",
                "user": user,
            }
        )

    def is_available(self):
        return not self.is_borrowed

    def get_book_info(self):
        return {
            "title": self.title,
            "author": self.author,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": self.borrowed_by,
            "borrow_count": self.borrow_count,
        }

    def _validate_required_text(self, value, field_name):
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a string")

        normalized_value = value.strip()

        if not normalized_value:
            raise ValueError(f"{field_name} is required")

        return normalized_value
