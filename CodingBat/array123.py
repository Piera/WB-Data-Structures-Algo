
# Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere. 

# array123([1, 1, 2, 3, 1]) -> True
# array123([1, 1, 2, 4, 1]) -> False
# array123([1, 1, 2, 1, 2, 3]) -> True

def array123(nums):
	subarray_count = 0
	for i in range(len(nums)-1):
		if nums[i:i+3] == [1,2,3]:
			subarray_count += 1
	if subarray_count != 0:
		print "True"
		return True
	else:
		print "False"
		return False



array123([1, 1, 2, 3, 1]) 
array123([1, 1, 2, 4, 1]) 
array123([1, 1, 2, 1, 2, 3]) 
