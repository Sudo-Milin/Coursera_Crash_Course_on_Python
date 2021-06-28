### The highlight_word function changes the given word in a sentence to its upper-case version. 
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". 
# Can you write this function in just one line?

# Function defined. 
def highlight_word(sentence, word):
	# The upper() method of string converts the given string to UPPERCASE. replace() method of string is used to replace the original word to its new uppercased version. The replace() method take two arguments; 1) string to be changed, 2) string to be replaced with. 
	return(sentence.replace(word, word.upper()))

# Function called
print(highlight_word("Have a nice day", "nice"))
# Function called
print(highlight_word("Shhh, don't be so loud!", "loud"))
# Function called
print(highlight_word("Automating with Python is fun", "fun"))
