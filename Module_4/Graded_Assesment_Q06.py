### Taylor and Rory are hosting a party.
# They sent out invitations, and each one collected responses into dictionaries, with names of their friends and how many guests each friend is bringing. 
# Each dictionary is a partial list, but Rory's list has more current information about the number of guests. 
# Fill in the blanks to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries. 
# Then print the resulting dictionary.

# Function defined
def combine_guests(guests1, guests2):
  # An empty dictionary is created to store final data.
  new_dict={}
  # To add data to new dictionary update() method of dictionary is used. It baically adds data to a dictionary from other dictionary. Moreover it updates the value to a current key if present to a new value that is present in the dictionary givin as argument in update() method.
  # Firstly the data from dictionary of Taylor is added.
  new_dict.update(guests2)
  # Then Rory's data is added as it updates the value of Taylor's data if any.
  new_dict.update(guests1)
  # Lastly the new dictionary is returned.
  return new_dict

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
# Function call
print(combine_guests(Rorys_guests, Taylors_guests))
