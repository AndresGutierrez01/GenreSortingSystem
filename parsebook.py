import nltk


class Book:
	def __init__(self, name):
		book = open("./BookFiles/" + name)
		raw = book.read()
		self.text = nltk.word_tokenize(raw)


	def get_count(self, *words):

		if len(words) == 1:
			return self.text.count(words[0])

		arr = []
		for word in words:
			arr.append(self.text.count(word))
		return arr

