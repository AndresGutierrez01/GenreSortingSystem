import glob
import numpy as np
from parsebook import Book
import bookNBC


def getData(loveBooksPath, horrorBooksPath):
    loveBooks = []
    horrorBooks = []

    lovefiles = glob.glob(loveBooksPath)
    for file in lovefiles:
        book = Book(file)
        loveBooks.append(book)

    horrorfiles = glob.glob(horrorBooksPath)
    for file in horrorfiles:
        book = Book(file)
        horrorBooks.append(book)

    words = ["love", "adore", "kiss", "beloved", "happiness", "scary", "horror", "blood", "death", "creepy"]

    loveValues = Book.get_counts(loveBooks, words)

    horrorValues = Book.get_counts(horrorBooks, words)

    loveData = np.insert(loveValues, len(words), values=0, axis=1)
    horrorData = np.insert(horrorValues, len(words), values=1, axis=1)

    data = []
    data = np.concatenate((loveData, horrorData), axis=0)

    return data