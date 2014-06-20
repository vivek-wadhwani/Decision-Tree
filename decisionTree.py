'''
@author: Vivek
'''

import sys
from entropy import *

import sys
from recursive import *

import sys
from getFiles import *


def accuracy(algoclassification, targetClassification):
    matching_count = 0.0

    for alg, target in zip(algoclassification,targetClassification):
        if alg == target:
            matching_count += 1.0

    #print len(algoclassification)
    #print len(targetClassification)
    return (matching_count / len(targetClassification)) * 100

def print_decisionTree(decisiontree, str):
    

    if type(decisiontree)== dict:
        #print "%s%s = " % (str,decisiontree.keys()[0]),
        for item in decisiontree.values()[0].keys():
            print "%s%s = %s" % (str, decisiontree.keys()[0],item),
            print " : "
            #print "%s%s = " % (str,decisiontree.keys()[1]),
            
            print "||",
            #print "%s = " % (str,decisiontree.values()[0]),
            #print "%s%s = " % (str,decisiontree.keys()[0]),
            print_decisionTree(decisiontree.values()[0][item],str + "  ")
    else:
        print "%s : %s" % (str, decisiontree)

if __name__ == "__main__":

    trainFile = trainingFile()
    testFile = testingFile()
    decisiontree, classifyTrain, classifyTest, setOfGivenTrainClassData, setOfGivenTestClassData = run_app(trainFile,testFile)
    print_decisionTree(decisiontree,"")
    print " Accuracy of training set (%s instances) = " % len(setOfGivenTrainClassData),
    print accuracy(classifyTrain, setOfGivenTrainClassData)
    print " Accuracy of test set (%s instances) = " % len(setOfGivenTestClassData),
    print accuracy(classifyTest, setOfGivenTestClassData)
