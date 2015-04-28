# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo". 

# string_bits('Hello') -> 'Hlo'
# string_bits('Hi') -> 'H'
# string_bits('Heeololeo') -> 'Hello'

def string_bits(str):
	i = 0
	new_str = []
	while len(str[i:]) >= 1:
		new_str.append(str[i])
		i = i + 2
		print new_str
	print "".join(new_str)
	return "".join(new_str)

string_bits('Hello') 
string_bits('Hi') 
string_bits('Heeololeo') 
# string_bits('hxaxpxpxy') -> 'happy'
string_bits('hxaxpxpxy')