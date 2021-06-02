### The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2, up to and including the maximum that's passed into the function. 
# For example, even_numbers(6) returns “2 4 6”. Fill in the blank to make this work.


def even_numbers(maximum):
	# Initially an empty variable 'return_string' is created to store the result.
	return_string = ""
	# A loop for number starting from 1 to the user given number (+1 because python does not include the last element in range). 
	for x in range (1,maximum+1):
		# For every iteration it checks if the value 'x' is divisible by 2 or not (checked by using module operator which returns the value of the remainder in the division operation).
		if x%2==0:
			# If it is divisible then it is added to the 'return_string' variable with a space after it
			return_string += str(x) + " "
	# At last the the value of 'return_string' is returned along with strip() method which removes white spaces from starting and ending of string
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed
