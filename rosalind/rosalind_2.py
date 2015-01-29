def count_nucleotides():
	transcribed = []
	RNA = open('rosalind_rna.txt', 'r')
	RNA_read = RNA.read()
	RNA_string = RNA_read.strip()
	# RNA_string = 'GATGGAACTTGACTACGTAAATT'
	for letter in RNA_string:
		if letter == 'T':
			letter = 'U'
		transcribed.append(letter)
		result = "".join(transcribed)
	print result

count_nucleotides()