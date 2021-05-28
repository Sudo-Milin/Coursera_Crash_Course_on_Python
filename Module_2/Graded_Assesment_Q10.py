### The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). 
# Complete the body of the function so that it returns the right number.
# Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.

def fractional_part(numerator, denominator):
	# A condition which checks the value of denominator, if the value is greater than 0 then the if block is executed. 
	if denominator>0:
		# this 'if' block returns value of the division from which the integer part is substracted. It is done by substracting the value of division from value of floor division, which returns only the integer part of the division.
		return ((numerator/denominator)-(numerator//denominator))
	# If the condition of 'if' block is not satisfied then else block is executed, which returns '0'.
	else:
		return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
