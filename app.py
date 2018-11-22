from parsebook import Book
from bookNBC import bookNBC


b = Book("Anna Karenin.txt")


values = b.get_count("ice")

print(values)