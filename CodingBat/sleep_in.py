
# The parameter weekday is True if it is a weekday, 
# and the parameter vacation is True if we are on vacation. 
# We sleep in if it is not a weekday or we're on vacation. 
# Return True if we sleep in. 

# sleep_in(False, False) -> True
# sleep_in(True, False)  -> False
# sleep_in(False, True)  -> True
# sleep_in(False, False) -> True

def sleep_in(weekday, vacation):
	# if weekday == False and vacation == False:
	# 	print "True"
	# 	return True
	# if weekday == True and vacation == False:
	# 	print "False"
	# 	return False
	# if weekday == False and vacation == True:
	# 	print "True"
	# 	return True
	# if weekday == False and vacation == False:
	# 	print "True"
	# 	return True
	# if weekday == True and vacation == True:
	# 	print "True"
	# 	return True
	print (not weekday or vacation)
	return(not weekday or vacation)

sleep_in(False, False) 
sleep_in(True, False)  
sleep_in(False, True) 
sleep_in(False, False) 