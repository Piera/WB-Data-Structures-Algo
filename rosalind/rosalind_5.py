DNA = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'

# s = 'A - 13, B - 14, C - 29, M - 99'
# dict(e.split(' - ') for e in s.split(','))
# {'A': '13', 'C': '29', 'B': '14', 'M': '99'}

def find_percentage(DNA):
	CG_counter = 0
	for letter in DNA:
		if letter == 'C' or letter == 'G':
			CG_counter += 1
	print CG_counter
	CG_percentage = (float(CG_counter) / float(len(DNA))) * 100
	print CG_percentage	
	return CG_counter

find_percentage(DNA)

def load_dictionary():
	DNA_formatted = open('rosalind_gc.txt', 'r')
	DNA_read = DNA_formatted.read()
	DNA_split = DNA_read.split('\n')
	counter = 1
	for info in DNA_split:
		print counter
		print info[0]
		counter += 1
		# if info[0] == '>':
		# 	print info
	# DNA_dict = dict(e.split('\n',1) for e in DNA_read.split('>'))
	# print DNA_dict
	# print DNA_try

load_dictionary()