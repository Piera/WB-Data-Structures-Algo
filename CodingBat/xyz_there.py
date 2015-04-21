# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not. 

# xyz_there('abcxyz') -> True
# xyz_there('abc.xyz') -> False
# xyz_there('xyz.abc') -> True

def xyz_there(str):
	i = 0
	status = False

	while i < len(str):
		i = str.find('xyz', i)
		if i == -1:
			break
		index_check = i - 1
		if str[index_check] == ".":
			if status != True:
				status = False
		else:
			status = True
		i += 1
	print status
	return status

# xyz_there('abc.xyz')
xyz_there('abc.xyzxyz')
