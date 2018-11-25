import numpy as np
from getData import getData
from bookNBC import bookNBC
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

loveBooksPath = './LOVE BOOKS/*.txt'
horrorBooksPath = './HORROR BOOKS/*.txt'
numAttributes, data = getData(loveBooksPath, horrorBooksPath)


accuracy=[]
k=4
foldsize = int(len(data)/k)
for j in range(10):
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
            predicted.append(bookNBC(traind, test[[j],:numAttributes], numAttributes, 2))

        accuracy.append(accuracy_score(testy, predicted))

for i in range(len(accuracy)):
    print("Accuracy in try ",i,": ",accuracy[i])
plt.plot(accuracy,'ro')
plt.ylabel('Accuracy')
plt.show()


