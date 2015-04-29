# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string. 

# end_other('Hiabc', 'abc') -> True
# end_other('AbC', 'HiaBc') -> True
# end_other('abc', 'abXabc') -> True

def end_other(a, b):
	a = a.lower()
	b = b.lower()
	if a.endswith(b):
		print True
		return True
	if b.endswith(a):
		print True
		return True
	else:
		print True
		return False

# end_other('abc', 'abXabc')
# end_other('AbC', 'HiaBc')
end_other('Hiabc', 'abc')