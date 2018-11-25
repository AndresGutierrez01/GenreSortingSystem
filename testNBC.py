import numpy as np
from getData import getData
from bookNBC import bookNBC
from sklearn.metrics import accuracy_score

loveBooksPath = './LOVE BOOKS/*.txt'
horrorBooksPath = './HORROR BOOKS/*.txt'
data = getData(loveBooksPath, horrorBooksPath)



k=4
foldsize = int(len(data)/k)
for j in range(1):
    np.random.shuffle(data)
    for i in range(k):
        predicted = []
        testy = []
        a=i*foldsize
        b=(i+1)*foldsize
        traind = np.delete(data, np.s_[a:b], axis=0)

        test=data[a:b,:]

        testy = data[a:b, [-1]]


        for j in range(len(test)):
            # print("predicted class:", bookNBC(traind, test[[j],:10], 10, 2))
            # print(test[[j],10])
            predicted.append(bookNBC(traind, test[[j],:10], 10, 2))

        print('Accuracy', accuracy_score(testy, predicted))


