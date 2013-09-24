# Author: Hoang Van Thang
# date: 15/9/2013
"""
    This program discript about some check condition to become a triangle.
"""
import math

def checkinput(edge1, edge2, edge3):
    if (type(edge1) in [float, int, long] and type(edge1) in [float, int, long] and type(edge1) in [float, int, long]
        and (edge1 >= 0 and edge1 <= 2**32-1) and (edge2 >= 0 and edge2 <= 2**32-1)
        and (edge3 >= 0 and edge3 <= 2**32-1)):
        return 1;
    else: 
        return 0;
    
def NormalTriangle(edge1, edge2, edge3):
    if ( edge1 + edge2 > edge3 and edge1+edge3 > edge2 and edge2+edge3 > edge1 ):  
        return 1
    else: return 0
    
def CanTriangle(edge1, edge2, edge3):
    if(edge1 == edge2 or edge2 == edge3 or edge1 == edge3):
        return 1
    else: return 0

def SquareTriangle(edge1, edge2, edge3):
    if (abs(edge2**2 + edge3**2 - edge1**2) < 10**-9 or abs(edge1**2 + edge2**2 - edge3**2) < 10**-9 or
        abs(edge1**2 + edge3**2 - edge2**2) < 10**-9):
        return 1
    else: return 0
        
def detect_triangle(edge1, edge2, edge3):
    if(checkinput(edge1, edge2, edge3)):
        if( edge1 == edge2 == edge3):
            return "tam giac deu"
        elif (NormalTriangle(edge1, edge2, edge3) and CanTriangle(edge1, edge2, edge3)
        and SquareTriangle(edge1, edge2, edge3)):
            return "tam giac vuong can"
        elif (NormalTriangle(edge1, edge2, edge3) and CanTriangle(edge1, edge2, edge3)):
            return "tam giac can"
        elif(NormalTriangle(edge1, edge2, edge3) and SquareTriangle(edge1, edge2, edge3)):
            return "tam giac vuong"
        elif (NormalTriangle(edge1, edge2, edge3)):  
            return "day la tam giac"
        else:
            return "day khong la tam giac"
    else:
        return "dau vao khong hop le. Vui long nhap lai!"
        
    
    
    
    
    
    
    
    
    