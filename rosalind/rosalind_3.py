def reverse_complement():
	transcribed = []
	DNA = open('rosalind_revc.txt', 'r')
	DNA_read = DNA.read()
	DNA_string = DNA_read.strip()
	# DNA_string = 'AAAACCCGGT'
	for letter in DNA_string:
		if letter == 'A':
			letter = 'T'
		elif letter == 'T':
			letter = 'A'
		elif letter == 'C':
			letter = 'G'
		elif letter == 'G':
			letter = 'C'
		transcribed.append(letter)
		result = "".join(reversed(transcribed))
	print result

reverse_complement()
# Sample output ACCGGGTTTT