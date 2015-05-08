# Using the Python language, have the function SecondGreatLow(arr) 
# take the array of numbers stored in arr and return the second 
# lowest and second greatest numbers, respectively, separated by a space. 
# For example: if arr contains [7, 7, 12, 98, 106] the output should be 12 98. 
# The array will not be empty and will contain at least 2 numbers. 
# It can get tricky if there's just two numbers! 

def SecondGreatLow(arr): 
	arr = sorted(arr)
	arr_list = []
	for i in range(len(arr)):
		if arr[i] not in arr_list:
			arr_list.append(arr[i])
	if len(arr_list) == 3:
		a = str(arr_list[1])
		b = str(arr_list[1])
	if len(arr_list) == 2:
		a = str(arr_list[1])
		b = str(arr_list[0])
	elif len(arr_list) == 1:
		a = str(arr_list[0])
		b = str(arr_list[0])
	else:
		a = str(arr_list[1])
		b = str(arr_list[-2])

	print a + " " + b
	return a + " " + b

SecondGreatLow([1, 42, 42, 42, 180]) # Output = "42 42"
SecondGreatLow([4, 90]) # Output = "90 4"

# When the input was (2,2,2,5,5,5,6) your output was incorrect.

SecondGreatLow([2,2,2,5,5,5,6])

# When the input was (7, 7, 90, 1000003) your output was incorrect.

SecondGreatLow([7, 7, 90, 1000003])

# When the input was (80, 80) your output was incorrect.

SecondGreatLow([80, 80])