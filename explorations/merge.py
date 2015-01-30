B = [1,3,4,6,7,9,11,89]
C = [2,5,8,10,12,13,15,110]
D = []

def merge(B, C, D):
	i = 0
	j = 0
	while i < len(B) and j < len(C):
		if B[i] < C[j]:
			D.append(B[i])
			i += 1
		else:
			D.append(C[j])
			j += 1
	D += B[i:]
	D += C[j:]
	print D
	return D

merge(B, C, D)

# -------------

lst = [44, 34, 65, 2, 49, 100, 1, 2, 3, 4, 67]



def merge_sort(lst):

	if len(lst) <= 1:
		# print lst
		return lst

	lst1 = merge_sort(lst[:len(lst)/2])
	print lst1

	lst2 = merge_sort(lst[len(lst)/2:])
	print lst2

	results = []

	while len(lst1) > 0 and len(lst2) > 0:
		if lst1[0] < lst2[0]:
			results.append(lst1.pop(0))
		elif lst2[0] <= lst1[0]:
			results.append(lst2.pop(0))
	results.extend(lst1)
	results.extend(lst2)

	print results
	return results

merge_sort(lst)




