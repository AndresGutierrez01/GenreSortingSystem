import glob
import numpy as np
from parsebook import Book
import bookNBC


def getData(loveBooksPath, horrorBooksPath):
    loveBooks = []
    horrorBooks = []

    lovefiles = glob.glob(loveBooksPath)
    for file in lovefiles:
        book = Book(file,"love")
        loveBooks.append(book)

    horrorfiles = glob.glob(horrorBooksPath)
    for file in horrorfiles:
        book = Book(file,"horror")
        horrorBooks.append(book)


    words = ["rose", "man", "like", "miss", "love", "smiles","around","hell", "something", "horror", "blood", "saw"]

    loveValues = Book.get_counts(loveBooks, words)
    horrorValues = Book.get_counts(horrorBooks, words)

    numattributes=len(words)

    loveData = np.insert(loveValues, numattributes, values=0, axis=1)
    horrorData = np.insert(horrorValues, numattributes, values=1, axis=1)

    data = []
    data = np.concatenate((loveData, horrorData), axis=0)



    return numattributes, data