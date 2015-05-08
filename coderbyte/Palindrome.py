def Palindrome(str):
	str = str.replace(" ", "")
	print str
	status = "true"
	constant = len(str)/2
	for i in range(constant):
		for j in range(1, constant+1):
			print i
			if str[i] == str[-j]:
				status = "true"
			else:
				status = "false"
	print status
	return status

# Palindrome("eyeeye")
# Palindrome("This")
# Palindrome("eye")
Palindrome("never odd or even") 
# Palindrome(str)
# Palindrome(str)
# Palindrome(str)
