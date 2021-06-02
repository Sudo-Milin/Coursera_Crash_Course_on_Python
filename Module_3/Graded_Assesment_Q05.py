### The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise. 
# Fill in the blanks to make this work correctly.

def counter(start, stop):
	# An alias of 'start' parameter 'x' is created so that the value of 'start' does not change throughout the program. 
	x = start
	# If the value of 'start' is greater than the value of 'stop' then a variable 'return_string' is initalized and a string saying 'Counting down' is stored to it just to let user know during output.
	if start>stop:
		return_string = "Counting down: "
		# Now while the value of 'x' is still greater than or equal to the value of 'stop', it adds the value of 'x' to the 'return_string' variable.
		while x >= stop:
			return_string += str(x)
			# After that it is checked that if the value of 'x' is greater than the value of 'stop'. NOTE: First we checked that is value is greater than or equal, but this time it is only greater than.
			# The logic is simple, if the value of 'x' is greater than there is some more values to be encountered during next iteration, so if its true then and only then we will add a ',' (comma) after the pervious entry.
			if (x > stop):
				return_string += ","
			# At last the value of 'x' is decreamented by one.
			x-=1
	# If the value of 'stop' is greater than the value of 'start' then a variable 'return_string' is initalized and a string saying 'Counting up' is stored to it just to let user know during output.
	else:
		return_string = "Counting up: "
		# Now while the value of 'x' is still smaller than or equal to the value of 'stop', it adds the value of 'x' to the 'return_string' variable.
		while x <= stop:
			return_string += str(x)
			# Similarly, that above logic is applied here too.
			if (x < stop):
				return_string += ","
			# At last the value of 'x' is increamented by one. 
			x+=1
	# If either of the block's while loop is terminated then the value of 'return_string' is returned.
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"
