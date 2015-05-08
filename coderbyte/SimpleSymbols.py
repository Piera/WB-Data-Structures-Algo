def SimpleSymbols(str): 
	letter = "abcdefghijklmnopqrstuvwxyz"
	if str[0] in "abcdefghijklmnopqrstuvwxyz" or str[-1] in "abcdefghijklmnopqrstuvwxyz":
		print "false"
		return "false"
	for i in range(1, len(str)-1):
		if str[i] in "abcdefghijklmnopqrstuvwxyz":
			if str[i-1] != "+" or str[i+1] != "+":
				return "false"
			else:
				print "true"
				return "true"

			
# There is a better way to do this with regex, I think!

SimpleSymbols("+d+=3=+s+") # true
SimpleSymbols("f++d+") # false
SimpleSymbols("+f++d+d") # false
SimpleSymbols("+f++d+d+") # true
SimpleSymbols("+d===+a+") # false