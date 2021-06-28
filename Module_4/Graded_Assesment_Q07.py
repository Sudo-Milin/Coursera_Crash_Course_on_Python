### Use a dictionary to count the frequency of letters in the input string.
# Only letters should be counted, not blank spaces, numbers, or punctuation. 
# Upper case should be considered the same as lower case. 
# For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

# Function defined
def count_letters(text):
  # An empty dictionary 'result' to store final result.
  result = {}
  # Each letter in text is iterated.
  for letter in text:
    # Convert each letter to lower case as sugessted.
    letter=letter.lower()
    # Now check if the letter is an alphabet of not.
    if letter.isalpha()==True:
      # If yes then check if it is present in result dictionary.
      if letter not in result:
        # If not present in result dictionary then intialize it in result dictionary.
        result[letter]=0
      # If already present in result dictionary then increament its value by one.  
      result[letter]+=1
  # Finally return the result.
  return result

# Function call
print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}
# Function call
print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
# Function call
print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
