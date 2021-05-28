### The longest_word function is used to compare 3 words. 
# It should return the word with the most number of characters (and the first in the list when they have the same length). 
# Fill in the blank to make this happen.

# The 'len()' function calculates the length of the given parameter

def longest_word(word1, word2, word3):
	# If the length of 'word1' is greater than or equal to length of 'word2' and 'word3' then the 'if' block is executed which initialize 'word' variable and stores value of 'word1' in it. Then execution breaks out of 'if' block and returns value of 'word' variable and execution stops.
	if len(word1) >= len(word2) and len(word1) >= len(word3):        
		word = word1
	# If the length of 'word2' is greater than or equal to length of 'word1' and 'word3' then the 'elif' block is executed which initialize 'word' variable and stores value of 'word2' in it. Then execution breaks out of 'elif' block and returns value of 'word' variable and execution stops.
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	# At last if all of the above conditions didn't satisfies then 'else' block is executed which initialize 'word' variable and stores value of 'word3' in it. Then execution breaks out of 'else' block and returns value of 'word' variable and execution stops.
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))
