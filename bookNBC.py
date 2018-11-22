import tensorflow as tf
import numpy as np



train = np.loadtxt('iris.csv', delimiter=',', dtype = np.float32) # first column is class label

k = 0
fold = 10
numtest = int(train.shape[0] / fold)


# np.random.shuffle(train)

# trainx = np.concatenate((train[0:numtest * k,:4],train[(numtest * k)+numtest:,:4]))
# trainy = np.concatenate((train[0:numtest * k,[4]],train[(numtest * k)+numtest:,[4]]))

trainx = train[0:149,:4]
trainy = train[0:149,[4]]

testx = train[[149],:4]
testy = train[[149],[4]]








# P(Ck)
classprior = np.count_nonzero(trainy[:,0] == 0)
print(classprior)


#P(x|Ck)
indeceswhereCk = np.argwhere(trainy == 0)
rowswhereCk = indeceswhereCk[:, 0]


totallikelihood = 1
for index, x in enumerate(testx[0,:]):
    xgivenCk = trainx[rowswhereCk, index]
    likelihood = np.count_nonzero(xgivenCk == x)
    # print(x, "is in it:", np.count_nonzero(trainx[:50,index] == x))
    print("likelihood:", likelihood)
    totallikelihood = totallikelihood * likelihood

print(totallikelihood)