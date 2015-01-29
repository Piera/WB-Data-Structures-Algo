def count_nucleotides():
	counting_dict = {}
	DNA = open('rosalind_dna.txt', 'r')
	DNA_read = DNA.read()
	DNA_string = DNA_read.strip()
	for letter in DNA_string:
		if letter not in counting_dict:
			counting_dict[letter]=1
		else:
			counting_dict[letter] = counting_dict[letter] + 1
	print counting_dict['A'], counting_dict['C'], counting_dict['G'], counting_dict['T']
	return counting_dict['A'], counting_dict['C'], counting_dict['G'], counting_dict['T']

count_nucleotides()




