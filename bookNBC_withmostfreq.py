#import tensorflow as tf
import numpy as np

# train = np.loadtxt('Data/freqdist.csv', delimiter=',', dtype="str")


#train => train values as a np array. The last column should be the class label.
#test => an np array that you want to determine the class label for. This array should just be one row
#numattributes => number of attributes in your thing
#numclasses => the number of classes. For right now this should just be 2 because we're only doing romance and horror so far :P
def bookNBC(train, test, numattributes, numclasses):
    trainx = train[:, :numattributes]
    trainy = train[:, [numattributes]].astype(int)

    # testx = test
    testx = test[:, :numattributes]

    likelihoodlist = []

    for k in range(numclasses):
        # P(Ck)
        classprior = np.count_nonzero(trainy[:, 0] == k)

        # P(x|Ck)
        indeceswhereCk = np.argwhere(trainy == k)
        rowswhereCk = indeceswhereCk[:, 0]  # this is an array that has the indices where the class is equal to k


        totallikelihood = 0
        for index, x in enumerate(testx[0, :]):
            xgivenCk = trainx[rowswhereCk, :]  # this is an array of the x values that are in the rows where the class is equal to k
            # print(xgivenCk)
            likelihood = np.count_nonzero(xgivenCk == x)  # the amount of times that x is in xgivenCk
            # print("word:",x,"likelihood in",k,":", likelihood)
            totallikelihood = totallikelihood + likelihood
        likelihoodlist.append(totallikelihood)

    # print("predicted class:", np.argmax(np.asarray(likelihoodlist), axis=0))
    prediction = np.argmax(np.asarray(likelihoodlist), axis=0)
    # print(likelihoodlist)
    return prediction