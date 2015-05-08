def LongestWord(sen): 
	sen_list = sen.split(" ")
	max_word = ""
	print len(max_word)
	for word in sen_list:
		bare_word = "".join(c for c in word if c not in ('!','.',':','&',',','"','/',':','[',']','~'))
		print bare_word
		print len(bare_word)
		if len(bare_word) > len(max_word):
			max_word = bare_word
	print max_word
	return max_word



  

LongestWord( "a confusing /:sentence:/[ this is not!!!!!!!~")