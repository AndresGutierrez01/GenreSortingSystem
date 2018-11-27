import glob
from parsebook import Book
from bookNBC_withmostfreq import bookNBC
import numpy as np
from getmostfreq import get_most_freq
# from bookNBC import bookNBC





get_most_freq(20, degree=5)


# loveBooksPath = './LOVE BOOKS/*.txt'
# horrorBooksPath = './HORROR BOOKS/*.txt'


# loveBooks = []
# horrorBooks = []

# lovefiles = glob.glob(loveBooksPath)
# for file in lovefiles:
#     book = Book(file,"love")
#     loveBooks.append(book)

# horrorfiles = glob.glob(horrorBooksPath)
# for file in horrorfiles:
#     book = Book(file,"horror")
#     horrorBooks.append(book)


# words = ["rose", "man", "like", "miss", "love", "smiles","around","hell", "something", "horror", "blood", "saw"]



# lovevalues = Book.get_counts(loveBooks, words)
# np_lovevalues = np.asarray(lovevalues)

# #adds the class label
# np_lovevalues = np.hstack((np_lovevalues,np.zeros((len(loveBooks),1))))

# #saves to file
# np.savetxt("Data/wordfreqs.csv", np_lovevalues, delimiter=",", fmt='%1.2f')



# horrorvalues = Book.get_counts(horrorBooks, words)
# np_horrorvalues = np.asarray(horrorvalues)

# #adds the class label
# np_horrorvalues = np.hstack((np_horrorvalues,np.ones((len(horrorBooks),1))))

# #appends the horror values to the file
# file = open("Data/wordfreqs.csv","a")
# np.savetxt(file, np_horrorvalues, delimiter=",", fmt='%1.2f')







# loveratios = Book.get_ratios(loveBooks, words)
# np_loveratios = np.asarray(loveratios)

# #adds the class label
# np_loveratios = np.hstack((np_loveratios,np.zeros((len(loveBooks),1))))

# #saves to file
# np.savetxt("Data/wordratios.csv", np_loveratios, delimiter=",", fmt='%1.2f')




# horrorratios = Book.get_ratios(horrorBooks, words)
# np_horrorratios = np.asarray(horrorratios)

# #adds the class label
# np_horrorratios = np.hstack((np_horrorratios,np.ones((len(horrorBooks),1))))

# #appends the horror values to the file
# file = open("Data/wordratios.csv","a")
# np.savetxt(file, np_horrorratios, delimiter=",", fmt='%1.2f')





































