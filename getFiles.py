'''

@author: Vivek
'''
import sys
from decisionTree import *
 

def testingFile():
    

    if len(sys.argv) < 3:
        print "Please enter name of test file - ",
        testFile = sys.stdin.readline().strip()
    
    try:
        testFile = open(testFile,"r")
    except IOError:
        print "The test file does not exist" %testFile
        sys.exit(0)

    return testFile


def trainingFile():
    

    if len(sys.argv) < 3:
        print "Please enter the training file - ",
        trainfile = sys.stdin.readline().strip()
        
    try:
        trainFile = open(trainfile,"r")
    except IOError:
        print "The train file does not exist" %trainfile
        sys.exit(0)

    return trainFile
