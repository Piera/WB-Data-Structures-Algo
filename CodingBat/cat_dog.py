# Return True if the string "cat" and "dog" appear the same number of times in the given string. 

# cat_dog('catdog') -> True
# cat_dog('catcat') -> False
# cat_dog('1cat1cadodog') -> True

# "The big brown fox is brown".count("brown")

def cat_dog(str):
	if str.count('cat') == str.count('dog'):
		print True
		return True
	else:
		print False
		return False

# cat_dog('1cat1cadodog')
# cat_dog('catdog') 
cat_dog('catcat') 