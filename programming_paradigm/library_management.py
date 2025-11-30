class Book:
    def __init__(self, title, author):
        self.title = title           # public
        self.author = author         # public
        self._is_checked_out = False # "private" (by convention)

    def check_out(self):
        """Mark the book as checked out. Returns True if successful, False if already checked out."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        """Mark the book as returned. Returns True if successful, False if it was not checked out."""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self):
        """Return True if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list of Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by title.
        Returns True if successful, False if not found or already checked out.
        """
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False  # book not found

    def return_book(self, title):
        """
        Return a book by title.
        Returns True if successful, False if not found or was not checked out.
        """
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  # book not found

    def list_available_books(self):
        """
        Return a list of (title, author) tuples for all available books.
        """
        return [(book.title, book.author) for book in self._books if book.is_available()]

        
