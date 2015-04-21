# Given a string, return a string where for every char in the original, there are two chars. 

# double_char('The') ->'TThhee'
# double_char('AAbb') ->'AAAAbbbb'
# double_char('Hi-There') -> 'HHii--TThheerree'

def double_char(str):
	double_array = []
	for letter in str:
		double_array.append(letter)
		double_array.append(letter)
	print "".join(double_array)
	return "".join(double_array)

double_char('Hi-There') 