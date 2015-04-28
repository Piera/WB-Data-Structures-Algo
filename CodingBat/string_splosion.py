# Given a non-empty string like "Code" return a string like "CCoCodCode". 

# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'

def string_splosion(str):
	splosion_list = []
	
	for i in range(1, len(str)+1):
		splosion_list.append(str[:i])
		i += 1
	print "".join(splosion_list)
	return "".join(splosion_list)

string_splosion('Code') 
string_splosion('abc') 
string_splosion('ab') 