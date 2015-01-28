def find_mode(lst):
	max_count = 0
	mode = 0
	nums_checked = []
	for i in range (len(lst)):
		count = 1
		for j in range (len(lst[i+1:])):
			if lst[i+j] == lst[i]:
				count += 1
			if count > max_count:
				max_count = count
				mode = lst[i]
	print mode
	return mode

array = [2, 3, 4, 4, 4, 4, 3, 5, 6, 7, 8, 9]

find_mode(array)