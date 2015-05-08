def ArithGeo(arr):

	arith_factor = arr[1]-arr[0]
	geo_factor = arr[1]/arr[0]
	i = 0
	j = 0

	for i in range(len(arr)-1):
		if arr[i+1] - arr[i] == arith_factor:
			i += 1
			arith_toggle = True
		else:
			arith_toggle = False

	for j in range(len(arr)-1):
		if arr[j+1]/arr[j] == geo_factor:
			j += 1
			geo_toggle = True
		else:
			geo_toggle = False

	if arith_toggle == True:
		print "Arithmatic"
	elif geo_toggle == True:
		print "Geometric"
	else:
		print "-1"

ArithGeo([1,5,9]) # Arithmatic
ArithGeo([10,110,210,310,410]) #"Arithmatic"
ArithGeo([10,110,210,310,410,511]) # -1
ArithGeo([1,2,3,4]) # "Arithmatic"
ArithGeo([5,10,15]) # "Arithmetic"
ArithGeo([2,4,16,24]) # -1
ArithGeo([2, 6, 18, 54]) # Geometric

# Not sure why some test cases failed in coderbyte. 