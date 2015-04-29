# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring). 

# last2('hixxhi') -> 1
# last2('xaxxaxaxx') -> 1
# last2('axxxaaxx') -> 2

def last2(str):
	substring_count = 0
	for i in range(len(str)-2):
		a = str[i:i+2]
		b = str[-2:]
		if a == b:
			print "yes"
			substring_count += 1
	print substring_count
	return substring_count



last2('hixxhi') 
last2('xaxxaxaxx') 
last2('axxxaaxx') 