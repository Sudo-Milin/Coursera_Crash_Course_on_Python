### What is the value of y at the end of the following code?

# This question in the asssesment is to test your knowledege regarding how much of the interpretation you can do yourself in your mind using the concepts you learnt and remember.

# A simple for loop with range of 10. NOTE: The value '10' won't be included.
for x in range(10):
    # An inner for loop with range equal to value of 'x'.
    for y in range(x):          # During the last iteration of outer for loop the value of 'x' would be '9'. Thus during the last iteration of inner for loop the maximum range is '9' i.e. '9' not included. 
        print(y)
# The result will be 1 2 3 4 5 6 7 8
# The upper limit of a range isn’t included, which means that the outer loop goes up to 9, so the highest upper limit for the inner loop is 9, which is also not included.

