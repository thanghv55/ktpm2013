'''
Created on Sep 24, 2013

@author: Tien Sinh
'''
import unittest
import math
from __init__ import detect_triangle

class Test(unittest.TestCase):
    
    def testName1(self):
        self.assertEqual(detect_triangle(-1,2,3), "dau vao khong hop le. Vui long nhap lai!")
    def testName2(self):    
        self.assertEqual(detect_triangle(-1,-2,3), "dau vao khong hop le. Vui long nhap lai!")
    def testName3(self):
        self.assertEqual(detect_triangle(1,2,2**32), "dau vao khong hop le. Vui long nhap lai!")
    def testName4(self):
        self.assertEqual(detect_triangle(-1,2,2**32), "dau vao khong hop le. Vui long nhap lai!")
    def testName5(self):
        self.assertEqual(detect_triangle(-1,-2,-3), "dau vao khong hop le. Vui long nhap lai!")
    def testName6(self):
        self.assertEqual(detect_triangle('a',1,2), "dau vao khong hop le. Vui long nhap lai!")
    def testName7(self):
        self.assertEqual(detect_triangle('a','b',2), "dau vao khong hop le. Vui long nhap lai!")
    def testName8(self):
        self.assertEqual(detect_triangle('a','b','c'), "dau vao khong hop le. Vui long nhap lai!")
    def testName9(self):
        self.assertEqual(detect_triangle('a',-2,'b'), "dau vao khong hop le. Vui long nhap lai!")
    def testName10(self):
        self.assertEqual(detect_triangle('a',2**32,'b'), "dau vao khong hop le. Vui long nhap lai!")
    def testName11(self):
        self.assertEqual(detect_triangle(1,2,3), "day khong la tam giac")
    def testName12(self):
        self.assertEqual(detect_triangle(10**-9,10**-9, 1), "day khong la tam giac")
    def testName13(self):
        self.assertEqual(detect_triangle(2,2.5,3), "day la tam giac")
    def testName14(self):
        self.assertEqual(detect_triangle(2**32 - 2, 2**32 -3, 4), "day la tam giac")   
    def testName15(self):
        self.assertEqual(detect_triangle(2,2,2), "tam giac deu")
    def testName16(self):
        self.assertEqual(detect_triangle(10**-9,10**-9,10**-9), "tam giac deu")
    def testName17(self):
        self.assertEqual(detect_triangle(2**32-1,2**32-1,2**32-1), "tam giac deu")
    def testName18(self):
        self.assertEqual(detect_triangle(math.sqrt(2),math.sqrt(2),math.sqrt(2)), "tam giac deu")
    def testName19(self):
        self.assertEqual(detect_triangle(1,1,math.sqrt(2)), "tam giac vuong can")
    def testName20(self):
        self.assertEqual(detect_triangle(math.sqrt(2),math.sqrt(2), 2), "tam giac vuong can")
    def testName21(self):
        self.assertEqual(detect_triangle(2,2,3), "tam giac can")
	def testName22(self):
        self.assertEqual(detect_triangle(2,3,2), "tam giac can")
    def testName23(self):
        self.assertEqual(detect_triangle(3,2,2), "tam giac can")
    def testName24(self):
        self.assertEqual(detect_triangle(1, 2**30, 2**30), "tam giac can")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()