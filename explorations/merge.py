B = [1,3,4,6,7,9,11,89]
C = [2,5,8,10,12,13,15,110]
D = []

def merge_sort(B, C, D):
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

merge_sort(B, C, D)



