### The show_letters function should print out each letter of a word on a separate line. 
# Fill in the blanks to make that happen.

def show_letters(word):
  # For loop interates each letter in the 'word' parameter that is passed during the function call.
	for letter in word:
    # For each letter encountered is printed.
		print(letter)
	
show_letters("Hello")
# Should print one line per letter
