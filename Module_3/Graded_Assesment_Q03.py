### Complete the function digits(n) that returns how many digits the number has.
# For example: 25 has 2 digits and 144 has 3 digits. 
# Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.

def digits(n):
  # A 'count' variable is initialized, which keeps the count of the number of digits in the 'n' parameter.
	count = 0
  # If the number is '0' then no need to do the further division process, and return 1 which is our result.
	if n == 0:
	  return 1
  # Now for the value of 'n' other than zero, the process of counting number of digit in 'n' is intiated. 
	while (n!=0):
    # 'count' variable is increamented as soon as the execution enters while loop, and is increamented every time while loop is executed.
		count += 1
    # Now the 'n' variable is assigned new value i.e; a floor division of number 'n' by 10. This results in a number 'n' but without the digit that was in the 'ones' place before this step. 
    n=n//10
    # As this floor division eleminates each digit in 'n' one by one the count vaariable keeps increasing, and eventually the value of 'n' becomes '0' and while loop breakes which returns the value of 'count' variable.
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1
