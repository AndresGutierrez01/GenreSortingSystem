import glob
from parsebook import Book
from bookNBC_withmostfreq import bookNBC
import numpy as np
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
# from bookNBC import bookNBC



data = np.loadtxt('Data/mostfreq.csv', delimiter=',', dtype="str")

numAttributes = np.size(data,1) - 1




accuracy=[]
k=10
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

        testy = data[a:b, [-1]].astype(int)

        print("\n\n_____________FOLD:",i,"________________\n")
        for j in range(len(test)):
            predict_tion = bookNBC(traind, test[[j],:numAttributes], numAttributes, 2)
            predicted.append(predict_tion)
       

        accuracy.append(accuracy_score(testy, predicted))

for i in range(len(accuracy)):
    print("Accuracy in try ",i,": ",accuracy[i])


print("Average accuracy:",sum(accuracy) / len(accuracy))
plt.plot(accuracy,'ro')
plt.ylabel('Accuracy')
plt.show()




# print("prediction:",predict_tion)
#             print("actual:",testy[j])
#             print("\n\n")


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
