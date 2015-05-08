def AlphabetSoup(str): 
	ord_list = []

	for char in str:
		char = ord(char)
		ord_list.append(char)
	ord_list.sort()
	print ord_list

	char_list = []
	for item in ord_list:
		char_list.append(chr(item))

	print "".join(char_list)
	return "".join(char_list)



AlphabetSoup("coderbyte") # Output = "bcdeeorty"
AlphabetSoup("hooplah") # Output = "ahhloop"

