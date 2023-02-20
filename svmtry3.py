# Student Name: TAI KOK HING
# Student ID: 1006592
# 11 Jan 2022 - Further enhancement at line 50

import numpy as np
from cvxopt import matrix, solvers
from sklearn.metrics import confusion_matrix, classification_report

trainDataSize = 25

# I encountered many problems after reading EXCEL into numpy, panda
# Therefore I cut and paste the IRIS data set as original 
# onto a *.txt file
myfilePath = 'D:/TKH/1_Project/1_1_Python/SUTD_TEST/IRIS.txt'

def buildData():
    mainData = []
    singleLineData = []

    with open(myfilePath,'r') as File1:

        FileContent = File1.readlines()
        header = FileContent.pop(0)
        for line in FileContent:

            cleanLine = line.replace('"','') # cleans the double comma at the head and tail of each row
            eachRowData = cleanLine.split()
                # for filtering away garbage in replies in R1 to R8
            i = 0
            for singleData in eachRowData:
                if (i < 4):
                    intData = float(singleData)
                    singleLineData.insert(i, intData)
                    i += 1
                else:
                    # Replace (Iris-setosa = +1, Iris-versicolor = -1, Iris-virginica = +2)
                    if singleData == 'Iris-setosa':
                        singleLineData.insert(i, int(1))
                    elif singleData == 'Iris-versicolor':
                        singleLineData.insert(i, int(-1))
                    else:
                        singleLineData.insert(i, int(2))

                    # singleLineData.insert(i, singleData)
                    # print(' THIS IS A STRING', singleData)
                    # print(singleLineData)
                    tempData = singleLineData[:]
                    mainData.append(tempData)
                    i = 0

            # for i in range (0, len(eachRowData)):
            #     del(singleLineData[0])
            # Thought I had tried all posible methods
            # what a enlightenment, thx for Py Institute
            del singleLineData[:]

        step = 50
        dummyData =[]
        for i in range (0,step):
            dummyData.append(mainData[i])
            dummyData.append(mainData[i+step])
            # dummyData.append(mainData[i+step+step])

    return dummyData


def buildTestData(sampleData,testRange):
    # for i in range (0, testRange):
    trainingData = sampleData[:testRange]
    testingData = sampleData[testRange:150]

    return trainingData, testingData

def computeAlpha(mytrainingData):
    # determine the size of vector X_n, minus one since knowing last col is y_n
    x_length = len(mytrainingData[0])-1
    # print(x_length)

    tempXn = []
    tempXm = []
    singleRowQ = []
    pList_of_List = []

    Yn = []
    for n in range (0,trainDataSize):
        
        Yn.insert(n,mytrainingData[n][x_length])

        for i in range (0, x_length):
            tempXn.insert(i,mytrainingData[n][i])
            # print(tempXn)
            # print(mytrainingData[n][i])

        for m in range (0,trainDataSize):
    
            for j in range (0, x_length):
                tempXm.insert(j,mytrainingData[m][j])
                    
            answer = 0
            # Vector X_n multiply X_m
            for k in range (0, x_length):
                answer = answer + tempXn[k] * tempXm[k] 

            # forming q Matrix element
            # y_n * y_m * X_n * X_m        
            answer = answer * mytrainingData[n][x_length] * mytrainingData[m][x_length]

            singleRowQ.insert(m,round(answer,2)) 
            
            for i in range (0, x_length):
                del(tempXm[0])

        for i in range (0, x_length):
            del(tempXn[0])
        
        tempRowQ = singleRowQ[:]
        pList_of_List.append(tempRowQ)

        for i in range (0, trainDataSize):
            del(singleRowQ[0])
 
    # print('-------------------------------')
    # print((pList_of_List))
    # print('-------------------------------')

    list_to_numpy_array = np.asarray(pList_of_List)

    P = matrix(list_to_numpy_array)
    # print('P is size:', end= '')
    # print(P.size)
    # print(P)

    # print('-------------------------------')
    # q = matrix([-1, -1, -1, -1],(x_length,1))

    qList = []

    for n in range (0,trainDataSize):
        qList.insert(n,-1.0)

    q = matrix([qList],(trainDataSize,1))
    # print('q is size:', end= '')
    # print(q.size)
    # print(q)

    # form G and h, because x_n must be greater than 0 

    GList = []
    hList = []

    k = 0
    for n in range (0,trainDataSize):
        hList.insert(n,0.0)
        for m in range (0,trainDataSize):
            if (n != m):
                GList.insert(k,0.0)
            else:
                GList.insert(k,-1.0)
            k += 1

    G = matrix([GList],(trainDataSize,trainDataSize))  
    # print('G is size:', end= '')
    # print(G.size)
    # print(G)

    h = matrix([hList],(trainDataSize,1))   
    # print('h is size:', end= '')
    # print(h.size)
    # print(h)

    sol = solvers.qp(P,q,G,h)
    print(sol['x'])
    print(sol['primal objective'])

        # Output of qp Function
            # Optimal solution found.
            # [ 1.30e-09]
            # [ 1.10e-02]
            # [ 5.96e-09]
            # [ 2.70e-01]
            # [ 2.19e-09]
            # [ 1.86e-09]
            # [ 4.25e-01]
            # [ 2.98e-09]
            # [ 1.20e-09]
            # [ 1.87e-09]

        # -0.35307871559266757
    # print(type(sol['x']))
    # <class 'cvxopt.base.matrix'>

    aList = []
    for l in range (0,trainDataSize):
        aList.insert(l,sol['x'][l])

    # print(sol['x'][3])
    # print(type(aList))
    # <class 'list'>
    # print(aList[3])
    # print(type(aList[3]))
    # <class 'float'>
    return aList, Yn

def computeMinWeight(mytrainingData, Yn, aList):
    singleRowW = []
    vector_wList = []
    minimizeWList = []

    x_length = len(mytrainingData[0])-1

    for p in range (0, trainDataSize):
        for j in range (0, x_length):
            answer = aList[p] * Yn[p] * mytrainingData[p][j]
            singleRowW.insert(j,answer) 

        # Achieve minimize (0.5*W^T*W)
        minimizeWList.insert(p,0.5*answer*answer)
        tempRowW = singleRowW[:]
        vector_wList.append(tempRowW)

        for i in range (0, x_length):
            del(singleRowW[0])

    # determine the lowest Weight  
    minWeight = min(minimizeWList)

    for index, weight in enumerate(minimizeWList):
        if(weight == minWeight):
            # print(index,weight)
            break

    for k in range (0, x_length):
        answer = vector_wList[index][k] * mytrainingData[index][k]

    b = 1/Yn[index] - answer

    return vector_wList[index], b
##########################

# MAIN PROGRAM STARTS HERE

##########################

# original data are sorted by 50 of Iris-setosa, 50 of Iris-versicolor and 50 of Iris-virginica
# this makes cutting training and test data meaningless if cut by
# top portion (i.e. only training on Iris-setosa)
# therefore buildData re-arranged by interwaving 
# the three groups (Iris-setosa, Iris-versicolor and Iris-virginica)
# and Replace (Iris-setosa = +1, Iris-versicolor = -1, Iris-virginica = +2)
# return the 150 data points as reconstructData
reconstructData = buildData()

# reconstructData further break into training and test data 
# 
mytrainingData, mytestData = buildTestData(reconstructData,trainDataSize)

mytestData_length = len(mytestData)

print('\n')
print('---------------------------------------------------------')
print(' (A) Split the data into training and test set randomly')
print('---------------------------------------------------------')
print('TRAINING DATA (SIZE = %d)'%trainDataSize)
# print(mytrainingData)
print('TESTING DATA (SIZE = %d)'%mytestData_length)
# print(mytestData)

# computeAlpha and returns alpha and y_n lists
aList, Yn =  computeAlpha(mytrainingData)

# With alpha and Bias, compute vector W that returns the 
# most minimum using 0.5*W^T*W to maximize the margin
smallestW_List, b = computeMinWeight(mytrainingData, Yn, aList)

print('\n')
print('---------------------------------------------------------')
print(' (B) Training and ﬁtting the model using the training data')
print('---------------------------------------------------------')
print('Computed minimum Weight',smallestW_List, 'and bias', b)
# print(smallestW_List)
# print(b)

predYnList = []
trueYnList = []
answer = 0.0
x_length = len(mytrainingData[0])-1
for c in range (0, mytestData_length):
    for k in range (0, x_length):
        answer = answer + smallestW_List[k] * mytestData[c][k]
   
    predYnList.insert(c,int(answer + b))
    trueYnList.insert(c,mytestData[c][x_length])

# print(predYnList)
# print(trueYnList)

print('---------------------------------------------------------')
print(' (C) Predicting the test set using the SVM regions')
print('---------------------------------------------------------')
print('\n')
print('----------------')
print('Confusion Matrix')
print('----------------')
print(confusion_matrix(trueYnList, predYnList))
# Output of Confusion Matrix
# [[ 0 45]
#  [ 0 45]]

print('\n')
print('---------------------')
print('Classification Report')
print('---------------------')
print(classification_report(trueYnList, predYnList))



