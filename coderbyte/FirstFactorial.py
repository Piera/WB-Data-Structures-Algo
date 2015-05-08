# Using the Python language, have the function 
# FirstFactorial(num) take the num parameter 
# being passed and return the factorial of it 
# (ie. if num = 4, return (4 * 3 * 2 * 1)). 
# For the test cases, the range will be between 1 and 18. 

def FirstFactorial(num):
	new_num = 1
	while num >= 2:
		total = new_num * (num)
		new_num = total
		num = num - 1



	print total
	return total

FirstFactorial(4) # 24
FirstFactorial(8) # 40320