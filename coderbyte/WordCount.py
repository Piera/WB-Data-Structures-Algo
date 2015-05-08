def WordCount(str):
	word_list = str.split(' ')
	counter = 0
	for word in word_list:
		counter += 1
	print counter
	return counter

WordCount("Hello World") #Output = 2
WordCount("one 22 three") #Output = 3