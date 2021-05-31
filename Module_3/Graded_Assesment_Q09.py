What is the value of y at the end of the following code?

for x in range(10):
    for y in range(x):
        print(y)
        
       
The upper limit of a range isn’t included, which means that the outer loop goes up to 9, so the highest upper limit for the inner loop is 9, which is also not included.

