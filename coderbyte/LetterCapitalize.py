def LetterCapitalize(str): 
	words = str.split(" ")
	new_words = []
	for word in words:
		word = word.title()
		new_words.append(word)
	capitalized_words = " ".join(new_words)
	print capitalized_words
	return capitalized_words


LetterCapitalize("hello world") # Output = "Hello World"
LetterCapitalize("i ran there") # "I Ran There"
LetterCapitalize("h3llo yo people") # Failed test case - why does it do this?