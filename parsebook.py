import nltk
from nltk.corpus import stopwords


class Book:
    def __init__(self, name, genre):
        # book = open("./" + genre + " BOOKS/" + name)
        book = open(name, encoding="utf8")
        raw = book.read()
        words = nltk.word_tokenize(raw)
        words = [word for word in words if word.isalpha()]
        words = [word.lower() for word in words]
        self.text = words
        self.name = name

    #use this function when you want to get the count of just one book
    #words => can either be a single string or a list of strings
    #if words is a list, then the function will return a list of counts
    def get_count(self, words):

        values = []
        if type(words) is list:
            for word in words:
                values.append(self.text.count(word))

        else:
            return self.text.count(words)

        return values


    #use this function when you want to get the words count over multiple books
    #books => list of Book objects
    #words => can either be a single string or a list of strings
    #this function will return a 2d array with the rows being the book and the columns are the words
    @staticmethod
    def get_counts(books, words):

        values = []
        if type(words) is list:
            for book in books:
                arr = []
                for word in words:
                    arr.append(book.text.count(word))
                values.append(arr)

        else:
            for book in books:
                    values.append([book.text.count(words)])

        return values




    #use this function when you want to get the ratios of words over multiple books
    #the values will be rounded to the nearest hundredth
    #books => list of Book objects
    #words => can either be a single string or a list of strings
    #this function will return a 2d array with the rows being the book and the columns are the ratios of the words
    @staticmethod
    def get_ratios(books, words):
        values = []
        if type(words) is list:
            for book in books:
                arr = []
                booklen = len(book.text)/1000
                for word in words:
                    ratio = book.text.count(word)/booklen
                    arr.append(round(ratio,2))
                values.append(arr)

        else:
            for book in books:
                booklen = len(book.text)/1000
                ratio = book.text.count(words)/booklen
                values.append([round(ratio,2)])

        return values





    def get_len(self):
        return len(self.text)






    def get_freq_dist(self, num):
        most_freq=[]
        word_list = [word for word in self.text if word not in stopwords.words('english')]
        fdist = nltk.FreqDist(word_list)

        for word, freq in fdist.most_common(num):
            most_freq.append(word)
            print(word,":",freq)
        return most_freq


