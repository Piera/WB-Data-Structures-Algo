# Using the Python language, 
# have the function SimpleAdding(num) add up all the numbers 
# from 1 to num. For the test cases, 
# the parameter num will be any number from 1 to 1000. 

def SimpleAdding(num):
	tot = 0
	for i in range(num+1):
		tot += i
	print tot
	return tot


SimpleAdding(12) #78
SimpleAdding(140) #9870
SimpleAdding(8)