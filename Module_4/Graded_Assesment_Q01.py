### The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". 
# The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. 
# For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". 
# Fill in the gaps to complete this function.

# Here the addrress string has simple and fixed format so, it is an easy task to simply seperate the first part of each address, as it would always be a number in this case.
def format_address(address_string):
  # Declare variables. The 'house_number' variable stores house number from address_string, while the 'street_name' variable stores the street name from the address string.  
  house_number=[]
  street_name=[]
  # Separate the address string into parts. This creates a list of all the words present and seperated by a 'space' in address_string. 
  add_list=address_string.split()
  # Traverse through the address parts i.e. the add_list is iterated
  for name in add_list:
    # Determine if the address part is the house number or part of the street name.
    # If the value of 'name' is equal to the first element in the add_list then it would definately be a number i.e. the house number in this case. If it is then it is stored in the house_number list.
      if name==add_list[0]:
        house_number.append(name)
    # Else if the value of 'name' is other than the first element in the add_list then it would surely be a street name in this case. It is then stored in the street_name list.     
      else:
        street_name.append(name)
  # before returning the result?
  
  # Return the formatted string. Finally the return string is created using the format string technique and join() method.  
  return "house number {} on street named {}".format(" ".join(house_number), " ".join(street_name) )


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
