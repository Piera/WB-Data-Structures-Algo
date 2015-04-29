
# Given an array of ints, return the number of 9's in the array. 

# array_count9([1, 2, 9]) -> 1
# array_count9([1, 9, 9]) -> 2
# array_count9([1, 9, 9, 3, 9]) -> 3

def array_count9(nums):
	nine_count = 0
	for num in nums:
		if num == 9:
			nine_count +=1
	print nine_count
	return nine_count

array_count9([1, 2, 9]) 
array_count9([1, 9, 9]) 
array_count9([1, 9, 9, 3, 9]) 
