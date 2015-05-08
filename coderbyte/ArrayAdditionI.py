def ArrayAdditionI(arr):
	target = max(arr)
	arr.remove(target)
	tracking = []
	check_list = ArrayRecurse(arr, target, tracking)
	if 'true' in check_list:
		print "true"
		return "true"
	else:
		print "false"
		return "false"

def ArrayRecurse(arr, target, tracking, partial=[]):
	if partial == []:
  		s=sum(partial)
  	else:
  		s=sum(partial)
		if s == target:
			print partial, " yes"
			tracking.append("true")
		if s != target:
			tracking.append("false")

	for i in range(len(arr)):
	    n = arr[i]
	    remaining = arr[i+1:]
	    ArrayRecurse(remaining, target, tracking, partial + [n])

	return tracking

ArrayAdditionI([1,2,3]) # true
ArrayAdditionI([5,7,16,1,2]) # false
ArrayAdditionI([3,5,-1,8,12]) # true
ArrayAdditionI([10,12,500,1,-5,1,0]) #false
ArrayAdditionI([31,2,90,50,7]) #true
ArrayAdditionI([54,49,1,0,7,4]) #true
ArrayAdditionI([31,2,90,50,7]) #true