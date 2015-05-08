def SwapCase(str):
	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQURSTUVWXYZ"
	char_list = []
	for char in str:
		if char in lower:
			char_list.append(char.upper())
		elif char in upper:
			char_list.append(char.lower())
		else:
			char_list.append(char)
	print "".join(char_list)

SwapCase("AAAH!")
SwapCase("*(UU(FSLF)")
