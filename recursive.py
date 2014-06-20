'''

@author: Vivek
'''
import sys
from entropy import *

def set_attributes(attributeList):
    
    attributesDict = {}
    attributeList = attributeList[:]
    attributes = []
    

    for i in xrange(0, len(attributeList)-1, 2):
        #append it to the list
        attributes.append(attributeList[i])
        # set attribute name as key to the number
        attributesDict[attributeList[i]] = attributeList[i+1] 

    return attributes, attributesDict



def run_app(trainFile, testFile):
    
    #read from training file
    linesInTrain = [lineTrain.strip() for lineTrain in trainFile.readlines()]
    attributesTrain = linesInTrain[0].replace("\t"," ").split(" ")

    
    targetAttributeTrain = "TrainingClass"
    
    
    #     linesInTrain.pop() 
    
    #once we have the attributes remove it from lines
    linesInTrain.reverse()
    # pops from end of list, hence the two reverses
    linesInTrain.pop() 
    #again reverse the list
    linesInTrain.reverse()        

    attrListTrain, attrDictTrain = set_attributes(attributesTrain)
    attrListTrain.append(targetAttributeTrain)
    #print attrListTrain
    attrDictTrain[targetAttributeTrain] = 2 # since its a binary classification 

    # prepare data
    trainData = []
    for lineTrain in linesInTrain:
        trainData.append(dict(zip(attrListTrain,[datum.strip() for datum in lineTrain.split("\t")])))
    
    
    #read the lines
    #from test file
    testingLines = [line.strip() for line in testFile.readlines()]
    
    attributes = testingLines[0].split(" ")
    targetAttribute = "TestingClass"
    
    #once we have the attributes remove it from lines
    testingLines.reverse()
    # pops from end of list, hence the two reverses
    testingLines.pop() 
    #again reverse the list
    testingLines.reverse()        

    attributeList, attrDict = set_attributes(attributes)
    attributeList.append(targetAttribute)
    #print attributeList
    
    # since its a binary classification
    attrDict[targetAttribute] = 2 

    # prepare data
    testData = []
    for line in testingLines:
        testData.append(dict(zip(attributeList,[datum.strip() for datum in line.split("\t")])))
        
    #print testData

    


    trainingTree = create_decision_tree(trainData, attrListTrain, targetAttributeTrain, gain)
    trainingClassification = classification_function(trainingTree, trainData)

    testTree = create_decision_tree(testData, attributeList, targetAttribute, gain)
    testClassification = classification_function(testTree, testData)

    # also returning the example classification in both the files
    givenTestClassification = []
    for row in testData:
        givenTestClassification.append(row[targetAttribute])

    givenTrainClassification = []
    for row in trainData:
        givenTrainClassification.append(row[targetAttributeTrain])

    return trainingTree, trainingClassification, testClassification, givenTrainClassification, givenTestClassification