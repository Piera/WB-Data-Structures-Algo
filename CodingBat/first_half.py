# Given a string of even length, 
# return the first half. So the string "WooHoo" yields "Woo". 

def first_half(str):
	half_index=len(str)/2
	print str[:half_index]
	return str[:half_index]


first_half('WooHoo') # 'Woo'
first_half('HelloThere') # 'Hello'
first_half('abcdef') # 'abc'