'''
Created on Oct 9, 2013

@author: Tien Sinh
'''
import unittest
import inspect
from input import main
    
doc = inspect.getdoc(main)
print doc
docs = doc.splitlines()
    
def split_variable(text):    
    variable,words = text.split(":")
    words=words.strip()
    numbers = words.replace("][", ";")
    number2 = numbers.replace("]", "")
    number3 = number2.replace("[", "")
    number = number3.split(";")  
    number1 = sorted(number, key=int)
    
    Validate={}
    i = 0 
    k=0
    while i<= len(number):
        numb1 = number[i]
        numb2 = number[i+1] 
        Validate[k]= (numb1, numb2)
        i = i+2
    print Validate
    
    final_array = []  
    b = int(0)
    while True:
        x = int(number1[b])
        y = int(number1[b+1])
        ans = (x + y)/2
        final_array.append(ans)
        b = b + 2
        if b == len(number1):
            break
    return final_array

def sum_array(L1,L2):
    length1=len(L1)
    length2=len(L2)
    b=[]
    for i in range(0,length1):
        for j in range(0,length2):
                str1 = L1[i]
                str2 = L2[j] 
                d = str(str1)+';'+ str(str2)
                b.append(d)
    return b
def test_Case(docs):
    bigArray=[]
    for line in docs:
        bigArray.append(split_variable(line))

    a=bigArray[0]
    for k in range(1,len(bigArray)):
        array_1 = bigArray[k]
        a = sum_array(a, array_1)
    return a

class Test(unittest.TestCase):
    pass

def test_generator(a,b):
    def test(self):
        self.assertEqual(a,b)
    return test

result = test_Case(docs)
result1={}
j = 0
for haiz in result:
    result1[j] = haiz.split(';')
    j = j+1
print result1

i=0

if __name__ == '__main__':
    for t in result1:
        test_name = 'testName'+str(i)
        test = test_generator(main(*result1[t]),"")
        setattr(Test, test_name, test)
        i = i+1
    unittest.main()
