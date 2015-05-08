def VowelCount(str): 
	vowel_count = str.count('a') + str.count('e') + str.count('i') + str.count('o') + str.count('u')
	print vowel_count
	

VowelCount("hello") # Output = 2
VowelCount("coderbyte") #Output = 3