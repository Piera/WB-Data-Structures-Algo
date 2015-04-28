# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count. 

# count_code('aaacodebbb') -> 1
# count_code('codexxcode') -> 2
# count_code('cozexxcope') -> 2

def count_code(str):
	counter = 0
	i = 0
	while "co" in str[i:]:
		j = str[i:].index("co")
		# print j
		if len(str[i + j:]) >=4 and str[i+ 3 + j] == "e":
			counter = counter + 1
		i = i + j + 3
	print counter
	return counter

count_code('aaacodebbb')
count_code('codexxcode')
count_code('cozexxcope')