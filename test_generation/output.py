'''
Created on Oct 9, 2013

@author: Tien Sinh
'''
import unittest
import inspect
import itertools
from input import main

    
doc = inspect.getdoc(main)
docs = doc.splitlines()

#swap two number
def swapTwoNumber(number1, number2):
    temp = number2
    number2 = number1
    number1 = temp
 
#sort two array have len equal
def sortTwoArray(minList, maxList):
    minList={}
    maxList={}
    for i in range(0,len(minList)):
        if minList[i] > minList[i+1]:
            swapTwoNumber(minList[i], minList[i+1])
            swapTwoNumber(maxList[i], maxList[i+1])
            
#normalization string
def normalization(text):    
    variable,words = text.split(":")
    words=words.strip()
    numbers = words.replace("][", ";")
    number2 = numbers.replace("]", "")
    number3 = number2.replace("[", "")
    number = number3.split(";")  
    
    minList = {}
    maxList = {}
    k = 0
    i = 0
    while i < len(number) :
        minList[k] = int(number[i])
        maxList[k] = int(number[i+1])
        i = i+2
        k = k+1
    sortTwoArray(minList, maxList)

    count = 0
    for i in range(0, len(minList)-1):
        if minList[i+1] <= maxList[i]:
            count = count + 1
    if count > 0:
        raise Exception("input wrong! plsease try again!")
    else:    
        number1 = sorted(number, key=int)
        final_array = []
        b = int(0)
        i = 0
        while True:
            x = int(number1[b])
            y = int(number1[b+1])
            ans = (x + y)/2
            final_array.append(ans)
            b = b + 2
            if b == len(number1):
                break
        return final_array

#combine cross two array 
'''def mergeArray(L1,L2):
    length1=len(L1)
    length2=len(L2)
    b=[]
    for i in range(0,length1):
        for j in range(0,length2):
                str1 = L1[i]
                str2 = L2[j] 
                d = str(str1)+';'+ str(str2)
                b.append(d)
    return b'''

#creates test case from a list
def testCase(docs):
    bigArray=[]
    i = 0
    for line in docs:
        bigArray.append(normalization(line))
        i = i+1
    a = list(itertools.product(*bigArray))
    return a

class Test(unittest.TestCase):
    pass

def test_generator(a,b):
    def test(self):
        self.assertEqual(a,b)
    return test

result = testCase(docs)

i=0
if __name__ == '__main__':
    for t in result:
        test_name = 'testName'+str(i)
        test = test_generator(main(*t),"tam giac deu")
        setattr(Test, test_name, test)
        i = i+1
    unittest.main()
