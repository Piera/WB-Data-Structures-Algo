# Given 2 strings, a and b, return the number of the positions 
# where they contain the same length 2 substring. 
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" 
# substrings appear in the same place in both strings. 

# string_match('xxcaazz', 'xxbaaz') -> 3
# string_match('abc', 'abc') -> 2
# string_match('abc', 'axc') -> 0

def string_match(a, b):
	min_length = min(len(a), len(b))
	counter = 0
	j = 2
	while j <= len(a):
		for i in range(min_length - 1):
			if a[i:j] == b[i:j]:
				counter += 1
			j += 1
	print counter
	return counter


string_match('aabbccdd', 'abbbxxd') 
# string_match('xxcaazz', 'xxbaaz') 
# string_match('aabbccdd', 'abbbxxd')
# string_match('aaxxaaxx', 'iaxxai')
# string_match('abc', 'abc') 
# string_match('abc', 'axc') 