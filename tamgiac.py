# Author: Hoang Van Thang
# date: 15/9/2013
"""
	This program discript about some check condition to become a triangle.
"""
def checkinput(edge1, edge2, edge3):
	if edge1 < 0 or edge1 > 2**32-1:
		#print "input error!"
		return 0
	elif edge2 < 0 or edge2 > 2**32-1:
		#print "input error!"
		return 0
	elif edge3 < 0 or edge3 > 2**32-1:
		#print "input error!"
		return 0
	else: 
		#print "input success!"
		return 1
	
#print checkinput(1,2,3)
#print checkinput(-1,2,3)
#print checkinput('a',2,3)

def sum(number1, number2):
	return number1 + number2
	
def NormalTriangle(edge1, edge2, edge3):
	if ( sum(edge1,edge2) > edge3 and sum(edge1,edge3) > edge2
		and sum(edge2,edge3) > edge1 ):  
		return 1
	else: return 0
	
def CanTriangle(edge1, edge2, edge3):
	if(edge1 == edge2 or edge2 == edge3 or edge1 == edge3):
		return 1
	else: return 0

def SquareTriangle(edge1, edge2, edge3):
	if ((edge2**2 + edge3**2 == edge1**2) or (edge1**2 + edge2**2 == edge3**2) or
		(edge1**2 + edge3**2 == edge2**2)):
		return 1
	else: return 0
		
def triangle(edge1, edge2, edge3):
	if(checkinput(edge1, edge2, edge3)):
		if( edge1 == edge2 == edge3):
			print "equilateral triangle!"
		elif (NormalTriangle(edge1, edge2, edge3) and CanTriangle(edge1, edge2, edge3)
		and SquareTriangle(edge1, edge2, edge3)):
			print "tam giac vuong can"
		elif (NormalTriangle(edge1, edge2, edge3) and CanTriangle(edge1, edge2, edge3)):
			print "tam giac can"
		elif(NormalTriangle(edge1, edge2, edge3) and SquareTriangle(edge1, edge2, edge3)):
			print "This is Square triangle!"
		elif (NormalTriangle(edge1, edge2, edge3)):  
			print "This is a triangle!"
		else:
			print "This isn't triangle!"
	else:
		print "input error! Please try again. thanks!"
		
print triangle(3,3,4)
	
	
	
	
	
	
	
	
	