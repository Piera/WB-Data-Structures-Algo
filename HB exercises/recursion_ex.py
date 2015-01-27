print "---------------------"

lst = [1, 2, 3, 4, 5, 6, 7]
print lst

# def reverse(lst):
# 	if lst == []:
# 		return []
# 	else:
# 		# print 'New list', new_list
# 		# x = lst.pop()
# 		# print x
# 		lst.append(lst.pop())
# 		reverse(lst)
# 	print lst

# def reverse(lst):
# 	if lst == []:
# 		return []
# 	else:
# 		temp = [lst.pop()]
# 		reverse(lst)
# reverse(lst)

def reverse(lst):
	if lst == []:
		return []
	else:
		temp = lst.pop(0)
		reverse(lst)
		lst.append(temp)
	print lst
	return lst


reverse(lst)

# -------------------

# def fibonacci(n):
# 	if n == 0 or n == 1:
# 		return n
# 	else:
# 		fibonacci(n-1)
#         print "Fibonacci ", x
#         return x
# fibonacci(5)

print "---------------------"

def fibonacci(n):
	# if n == 0 or n == 1:
	# 	return n
	# else:
	# 	n = (n-1) + (n-2)
	# 	print n
	if n == 0 or n == 1:
		return n
	else:
		n = fibonacci(n-1) + fibonacci(n-2)
		print n
		return n

fibonacci(5)

print "Fibonacci done, no errors"
print "---------------------"

# ----------------------

def count_up(n, target):
	if n < target+1:
		print "Count up! ", n
		count_up(n+1, target)

count_up(2, 7)

print "---------------------"

# ----------------------

def find(lst, i):
	# if lst[-1] == i:
	# 	print lst[-1]
	# 	return lst[-1]
	# else:
	# 	lst.pop()
	# 	find(lst, i)
	# 	print "Boo"
	# 	return None

	if lst != []:
		x = lst.pop()
		if x == i: 
			return x
		else:
			find(lst, i)
			return None
    # pass

# find([7, 2, 9, 9, 9, 656, 343, 24324324], 7)
find(["a", "b", "c"], "a")






