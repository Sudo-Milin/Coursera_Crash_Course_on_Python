### Complete the function by filling in the missing parts.
# The color_translator function receives the name of a color, then prints its hexadecimal value. 
# Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.


# The function checks the value of color and skips the 'if' block if it does not satisfies the condition. 
def color_translator(color):
	# If the condition of below block is satisfied it initalize the 'hex_color' variable and breaks further execution of 'elif' block and returns value of  'hex_color' variable.
	if color == "red":
		hex_color = "#ff0000"
	# If the condition of above block is not satisfied then it breaks out of above block and execute next 'elif' block which, if satisfies then initalize the 'hex_color' variable and breaks further execution of 'elif' block and returns value of  'hex_color' variable.
	elif color == "green":
		hex_color = "#00ff00"
	# If the condition of above block is not satisfied then it breaks out of above block and execute next 'elif' block which, if satisfies then initalize the 'hex_color' variable and breaks further execution of 'else' block and returns value of  'hex_color' variable.
	elif color == "blue":
		hex_color = "#0000ff"
	# If the condition of above block is not satisfied then it breaks out of above block and execute next 'else' block which finally initalize the 'hex_color' variable and returns value of 'hex_color' variable.
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown
