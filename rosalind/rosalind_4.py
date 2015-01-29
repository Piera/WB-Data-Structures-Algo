def fibonacci(n):
	k = 3
	if n == 0 or n == 1:
		return n
	else:
		n = fibonacci(n-1) + 3*fibonacci(n-2)
	return n

print fibonacci(28)