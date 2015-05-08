def LetterCountI(str):
	word_list = str.split(' ')
	for word in word_list:
		char_dict = {}
		word_score = {}
		word_score[word] = 0
		max_score = 0
		for char in word:
			if char not in char_dict:
				char_dict[char] = 1
				word_score[word] = 1
			else:
				char_dict[char] += 1
				word_score[word] += 1
				if word_score[word] > max_score:
					max_score = word_score[word]
		print char_dict
		print word_score
		print max_score

# THIS ONE NOT DONE YET! NEEDS MORE WORK.

LetterCountI("Hello apple pie") # Output = "Hello"
# LetterCountI("No words") # Output = -1
# LetterCountI("no words here")
# LetterCountI("I lied before")
# LetterCountI("red none yellow") 
# LetterCountI("a b c d ee") 