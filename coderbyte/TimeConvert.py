def TimeConvert(num): 
	print str(num/60) + ":" + str(num%60)
	return str(num/60) + ":" + str(num%60)

TimeConvert(126) # "2:6"
TimeConvert(45) # "0:45"