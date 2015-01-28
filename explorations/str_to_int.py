num_dict = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
test_str = '55876'

def str_to_index(dict, input_str):
	print input_str
	print type(input_str)
	idx = len(input_str)-1
	pow = 0
	final_num = 0
	while idx >= 0:
		digit = input_str[idx]
		val = dict[digit]
		final_num = final_num + val*(10**pow)
		idx -= 1
		pow += 1
	print final_num
	print type(final_num)
	return final_num

str_to_index(num_dict, test_str)