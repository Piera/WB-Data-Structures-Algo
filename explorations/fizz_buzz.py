# For fun, code fizz-buzz as fast as you can.

def fizz_buzz(num):
	for i in range(1, num+1):
		if i%15==0:
			print i, "fizz_buzz"
		elif i%5==0:
			print i, "fizz"
		elif i%3==0:
			print i, "buzz"

fizz_buzz(20)

# ------------------------------

# For fun, make a fancier fizz-buzz kind of thing.

# Walp.  Let's start out by making some sort of list...
# How about a list of random numbers (integers)
import random
randoms = random.sample(xrange(100), 30)
# xrange is pretty cool. From the docs: 
# "This is especially fast and space efficient for sampling from a large population"
# For example I can make a list of 30 random numbers between 0 and 100.
# Let's sort that list of numbers in place.
randoms.sort()
print "Sorted randoms", randoms

# Given a list of random numbers, generate a report of how many fizzes and buzzes and fizz_buzzes
# there are...
# Not that exciting but kind of fun to play with fizz_buzz for a few mins.
def fancy_fizz_buzz(randoms):
	fizz_buzz_count = 0
	fizz_count = 0
	buzz_count = 0
	for i in range(len(randoms)):
		if randoms[i]%15==0:
			print randoms[i], "fizz_buzz"
			fizz_buzz_count += 0
		elif randoms[i]%5==0:
			print randoms[i], "fizz"
			fizz_count+=1
		elif randoms[i]%3==0:
			print randoms[i], "buzz"
			buzz_count+=1
	print "Totals: fizz = ", fizz_count, ", buzz = ", buzz_count, ", fizz_buzz = ", fizz_buzz_count

fancy_fizz_buzz(randoms)


