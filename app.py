from parsebook import Book
import numpy as np
# from bookNBC import bookNBC


AK = Book("Anna-Karenin.txt")
TSAF = Book("'Tween-Snow-and-Fire.txt")
EMMA = Book("Emma.txt")
HHH = Book("Healing-Her-Heart.txt")
TROTN = Book("The-Return-of-The-Native.txt")

# books = np.array([AK,TSAF,EMMA,HHH,TROTN])
books = [AK, TSAF, EMMA, HHH, TROTN]
words = ["love","adore","kiss","thing"]


values = Book.get_counts(books, words)


print(values)


print(Book.get_ratios(books, words))



# print(AK.get_count(words))
# print(AK.get_len())


