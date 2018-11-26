import glob
from parsebook import Book
from bookNBC_withmostfreq import bookNBC
import numpy as np
# from bookNBC import bookNBC


words = ["love","anticipation","thing"]


loveBooks = []
horrorBooks = []

loveBooksPath = './LOVE BOOKS/*.txt'
horrorBooksPath = './HORROR BOOKS/*.txt'

lovefiles = glob.glob(loveBooksPath)
for file in lovefiles:
    book = Book(file,"love")
    loveBooks.append(book)

horrorfiles = glob.glob(horrorBooksPath)
for file in horrorfiles:
    book = Book(file,"horror")
    horrorBooks.append(book)





numattributes = 20
numsamples = 20

# freq_dist_list = np.empty(shape=[10,10])
# print(freq_dist_list)
word_freq_list = np.ones((1,numattributes))
for book in loveBooks:
	word_list = book.get_freq_dist(numattributes)
	word_list = np.asarray([word_list])
	# word_list = np.transpose(word_list)
	word_freq_list = np.concatenate((word_freq_list,word_list))

	print(word_list)
	print(word_freq_list)
	
	# freq_dist_list = np.concatenate((freq_dist_list,word_list))
	
	np.savetxt("Data/lovefreqdist.csv", word_freq_list, delimiter=",", fmt='%s')

love_words_list = word_freq_list.flatten('F')
word_freq_list_with_class = np.insert(word_freq_list, numattributes, values=0, axis=1)
np.savetxt("Data/mostfreq.csv", word_freq_list_with_class[1:], delimiter=",", fmt='%s')





word_freq_list = np.ones((1,numattributes))
for book in horrorBooks:
	word_list = book.get_freq_dist(numattributes)
	word_list = np.asarray([word_list])
	# word_list = np.transpose(word_list)
	print(word_list)
	word_freq_list = np.concatenate((word_freq_list,word_list))

	
	print(word_freq_list)
	
	# freq_dist_list = np.concatenate((freq_dist_list,word_list))
	np.savetxt("Data/horrorfreqdist.csv", word_freq_list, delimiter=",", fmt='%s')


horror_words_list = word_freq_list.flatten('F')

word_freq_list_with_class = np.insert(word_freq_list, numattributes, values=1, axis=1)
freqdistfile = open("Data/mostfreq.csv","a")
np.savetxt(freqdistfile, word_freq_list_with_class[1:], delimiter=",", fmt='%s')




# common_words = list(set(love_words_list) & set(horror_words_list))


# for cw in common_words:
# 	print(cw,":","LOVE:",list(love_words_list).count(cw),"___HORROR:",list(horror_words_list).count(cw))

# print(common_words)


# for book in loveBooks[21:]:
# 	testx = np.asarray([book.get_freq_dist(20)])
# 	prediction = bookNBC(loveBooks,testx,20,2)
# 	print("prediction:",prediction)
# 	print("actual: 0\n\n")

# for book in horrorBooks[21:]:
# 	testx = np.asarray([book.get_freq_dist(20)])
# 	prediction = bookNBC(loveBooks,testx,20,2)
# 	print("prediction:",prediction)
# 	print("actual: 1\n\n")
































