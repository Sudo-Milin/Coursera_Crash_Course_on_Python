### This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column). 
# Fill in the blanks so that calling multiplication_table(1, 3) will print out:

# 1 2 3 

# 2 4 6 

# 3 6 9

# This function takes two parameters 'start' which represents starting number of table and 'stop' which is a number upto which number you want to display table. 
def multiplication_table(start, stop):
	# A loop is intiated with 'x' iterator which iterates from 'start' value to 'stop' value (we have to add '+1' because python does not include the last element in the range.) 
	for x in range (start, stop+1):
		# Another loop is initiated inside the loop with 'y' iterator which also iterates from 'start' value to 'stop' value.
		for y in range (start, stop+1):
			# Using this logic of two for loop we can multipy every 'x' iterator by every 'y' iterator. Each iteration of 'x' is multiplied by each and every iteration of 'y', and this continues until 'x' iterator reaches the limit of range. 
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above
