### A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. 
# Drew was the first one to note which students arrived, and then Jamie took over. 
# After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. 
# Jamie emailed a follow-up, saying that her list is in reverse order. 
# Complete the steps to combine them into one list as follows: 
# the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

# Function defined. This function takes lists as arguments.
def combine_lists(list1, list2):
  # A new_list variable as an empty list is created to store a new list as per given instruction.
  new_list=[]
  # list2 i.e. Drews_list is added to the new_list using extend() method of list. I takes another list as argument and add that list to currrent variable.
  new_list.extend(list2)
  # For second list i.e. Jamies_list, firstly it should be reversed, so reverse() method of string is used. 
  list1.reverse()
  # Later Jamies_list is also added using the same extend() method.
  new_list.extend(list1)
  # Finally the new_list is returned as function's return statement. 
  return new_list  

# Function call
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
# Function call
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
