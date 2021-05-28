### Complete the body of the format_name function. 
# This function receives the first_name and last_name parameters and then returns a properly formatted string.
# Specifically:

# If both the last_name and the first_name parameters are supplied, the function should return like so:
# print(format_name("Ella", "Fitzgerald"))
# Name: Fitzgerald, Ella

# If only one name parameter is supplied (either the first name or the last name) , the function should return like so:
# print(format_name("Adele", ""))
# Name: Adele
# or
# print(format_name("", "Einstein"))
# Name: Einstein


# Finally, if both names are blank, the function should return the empty string:
# print(format_name("", ""))
# 


def format_name(first_name, last_name):
	#  If the 'first_name' parameter has value and also 'last_name' parameter has value then 'if' block is executed which initalize 'string' variable and stores value of 'last_name' & 'first_name' parameter in formatted way, then it returns value of string and execution stops.
	if first_name != "" and last_name != "":
		string="Name: "+ last_name + ", " + first_name
	# If the 'first_name' parameter has value and 'last_name' parameter has no value then 'elif' block is executed which initalize 'string' variable and stores value of 'first_name' parameter in formatted way, then it returns value of string and execution stops.
	elif first_name != "" and last_name == "":
		string="Name: " + first_name
	# If the 'first_name' parameter has no value and also 'last_name' parameter has value then 'elif' block is executed which initalize 'string' variable and stores value of 'last_name' parameter in formatted way, then it returns value of string and execution stops.
	elif first_name == "" and last_name != "":
		string="Name: " + last_name
	# At last if all of the above condition is not satisfied then the 'else' block is executed, which initialize 'string' variable and keeps is empty and returns value of string and execution stops.
	else:
		string=""
	
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
