class Book:
  """
  A class representing a book with title, author, and availability status.
  """
  def __init__(self, title, author):
    """
    Initializes a Book object with title, author, and availability (not checked out).

    Args:
      title (str): The title of the book.
      author (str): The author of the book.
    """
    self.title = title
    self.author = author
    self._is_checked_out = False  # Private attribute to track availability

  def check_out(self):
    """
    Marks the book as checked out (unavailable).
    """
    self._is_checked_out = True

  def return_book(self):
    """
    Marks the book as returned (available).
    """
    self._is_checked_out = False

  def is_available(self):
    """
    Returns True if the book is available, False otherwise.
    """
    return not self._is_checked_out

  def __str__(self):
    """
    Defines how a Book object is printed: title by author.
    """
    return f"{self.title} by {self.author}"

class Library:
  """
  A class representing a library that manages a collection of Book objects.
  """
  def __init__(self):
    """
    Initializes a Library object with an empty list to store books.
    """
    self._books = []

  def add_book(self, book):
    """
    Adds a Book object to the library's collection.

    Args:
      book (Book): The Book object to be added.
    """
    self._books.append(book)

  def check_out_book(self, title):
    """
    Attempts to check out a book by title, marking it unavailable if found.

    Args:
      title (str): The title of the book to be checked out.
    """
    for book in self._books:
      if book.title == title:
        if book.is_available():
          book.check_out()
          print(f"Successfully checked out '{title}'.")
        else:
          print(f"Sorry, '{title}' is already checked out.")
        return

    print(f"Book '{title}' not found in the library.")

  def return_book(self, title):
    """
    Attempts to return a book by title, marking it available if found.

    Args:
      title (str): The title of the book to be returned.
    """
    for book in self._books:
      if book.title == title:
        if not book.is_available():
          book.return_book()
          print(f"Successfully returned '{title}'.")
        else:
          print(f"'{title}' is already available in the library.")
        return

    print(f"Book '{title}' not found in the library.")

  def list_available_books(self):
    """
    Prints a list of all available books in the library.
    """
    print("Available books:")
    for book in self._books:
      if book.is_available():
        print(book)