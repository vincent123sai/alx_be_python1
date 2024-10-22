class Book:
  """
  A class representing a book with title, author, and publication year.
  """
  def __init__(self, title, author, year):
    """
    Initializes a Book instance with title, author, and year.

    Args:
      title (str): The title of the book.
      author (str): The author of the book.
      year (int): The publication year of the book.
    """
    self.title = title
    self.author = author
    self.year = year

  def __str__(self):
    """
    Returns a string representation of the book in a human-readable format.

    Returns:
      str: A string in the format "(title) by (author), published in (year)".
    """
    return f"{self.title} by {self.author}, published in {self.year}"

  def __repr__(self):
    """
    Returns a string that would recreate the Book instance.

    Returns:
      str: A string in the format "Book('{self.title}', '{self.author}', {self.year})".
    """
    return f"Book('{self.title}', '{self.author}', {self.year})"

  def __del__(self):
    """
    Prints a message when the Book instance is deleted.

    Note: Destructors in Python are not guaranteed to be called 
          due to garbage collection. 
    """
    print(f"Deleting {self.title}")
    
    
    from book_class import Book

def main():
  # Creating an instance of Book
  my_book = Book("1984", "George Orwell", 1949)

  # Demonstrating the __str__ method
  print(my_book)  # Expected to use __str__

  # Demonstrating the __repr__ method
  print(repr(my_book))  # Expected to use __repr__

  # Deleting a book instance to trigger __del__
  del my_book

if __name__ == "__main__":
  main()