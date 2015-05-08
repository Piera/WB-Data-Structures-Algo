import re

def ABCheck(str):
	toggle = "false"
    
	for i in range(len(str)):
		if str[i] == 'a':
			try: 
				if str[i+4] == 'b':
					toggle = "true"
					print toggle
					return toggle
			except:
				toggle = "false"
		
		elif str[i] == 'b':
			try: 
				if str[i+4] == 'a':
					toggle = "true"
					print toggle
					return toggle
			except:
				toggle = "false"
				
	print toggle
	return toggle


# Using regex; not supported in coderbyte

	# str = str.replace(" ", "")
	# m = re.search('[a]..[b]', str)
	# if m != None:
	# 	print "true"
	# 	return "true"
	# else:
	# 	print "false"
	# 	return "false"

ABCheck("after badly") # "false"
ABCheck("Laura sobs") # "true"
ABCheck("123adzvb")
ABCheck("abccccazzzb")
ABCheck("bzzza")
