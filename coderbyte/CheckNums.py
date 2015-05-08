# Using the Python language, have the function 
# CheckNums(num1,num2) take both parameters 
# being passed and return the string true if num2 is 
# greater than num1, otherwise return the string false. 
# If the parameter values are equal to each other then 
# return the string -1. 

def CheckNums(num1,num2): 
	if num1 == num2:
		print "-1"
		return "-1"
	elif num1 > num2:
		print "false"
		return "false"
	else:
		print "true"
		return "true"

CheckNums(8,8) # -1
CheckNums(4,8) # true
CheckNums(8,4) # false