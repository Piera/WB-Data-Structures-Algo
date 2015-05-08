def LetterChanges(str): 
	new_words = []
	for char in str:
		if char in "abcdefghijlmnopqrstuvwxy":
			new_char = (chr(ord(char)+1))
			if new_char in "aeiou":
				new_char = new_char.upper()
			new_words.append(new_char)
		else:
			new_words.append(char)
	new_words = "".join(new_words)
	print new_words
	return new_words


LetterChanges("hello*3") # Output = "Ifmmp*3"
LetterChanges("fun times!") # Output = "gvO Ujnft!"
LetterChanges("hello world")
LetterChanges("this long cake@&")