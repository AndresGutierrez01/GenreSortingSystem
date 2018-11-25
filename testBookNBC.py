#import tensorflow as tf
import numpy as np
from bookNBC import bookNBC



train = np.loadtxt('Data/iris.csv', delimiter=',', dtype = np.float32) # last column is class label

np.random.shuffle(train)


trainx = train[0:149,:]

testx = train[[149],:4]
testy = train[[149],[4]]

print(trainx)
print(testx)
print("--------")
print(testy)

numattributes = 4
numclasses = 3



print("predicted class:",bookNBC(trainx, testx, numattributes, numclasses))
print("testy:",testy)