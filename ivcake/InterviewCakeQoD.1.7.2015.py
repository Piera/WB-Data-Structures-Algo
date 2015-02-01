# I have an array stockPricesYesterday where:
# The indices are the time, as a number of minutes past trade opening time, which was 9:30am local time.
# The values are the price of Apple stock at that time, in dollars.
# For example, the stock cost $500 at 10:30am, so stockPricesYesterday[60] = 500.

# Write an efficient algorithm for computing the best profit 
# I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday. 
# For this problem, we won't allow shorting; you must buy before you sell.

# Questions:

# None, so far

# Sample array:
stockPricesYesterday = { 0:100, 1:500, 2:550, 3:200, 4:321, 5:332 }

# Sorted by value:
sorted_prices = sorted(stockPricesYesterday.items(), key=lambda x:x[1])
print sorted_prices

# A dictionary we can iterate through uses .iteritems:
for time,price in stockPricesYesterday.iteritems():
	print time, price

# Different direction: we need to go through the list once; 
#  sorting doesn't really get us there, since time is important.
min_price = stockPricesYesterday[0]
# print min_price
max_profit = 0
for time in range(len(stockPricesYesterday)):
	current_price = stockPricesYesterday[time]
	print current_price
	min_price = min(min_price, current_price)
	print "Min price: ", min_price, "current price: ", current_price
	max_profit = max(max_profit, current_price - min_price)
print "Max profit: ", max_profit




