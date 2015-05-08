def DashInsert(thing): 
	dashed_list = []
	str_iterable = str(thing)
	for i in range(len(str_iterable)):
		if int(str_iterable[i]) == 0:
			dashed_list.append("0")
		elif int(str_iterable[i])%2 > 0:
			if int(str_iterable[i+1])%2 > 0:
				dashed_list.append(str_iterable[i])
				dashed_list.append("-")
			else: 
				dashed_list.append(str_iterable[i])
		else:
			dashed_list.append((str_iterable[i]))
	ans = "".join(dashed_list)
	print ans
	return ans

#Need to re-do this one, too.  Some test cases failed.

DashInsert(99946) # Output = 9-9-946
DashInsert(56730) # Output = 567-30