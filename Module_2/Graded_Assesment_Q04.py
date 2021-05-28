### Students in a class receive their grades as Pass/Fail.
# Scores of 60 or more (out of 100) mean that the grade is "Pass". 
# For lower scores, the grade is "Fail". 
# In addition, scores above 95 (not included) are graded as "Top Score".
# Fill in this function so that it returns the proper grade.

# This function checks different conditions for value of score.
def exam_grade(score):
	# If the given condition is satisfied then the 'grade' variable is initalized and a string value is assigned to it then, it returns the value of 'garde' variable and execution is stopped.  
	if score>95:
		grade = "Top Score"
	# If the above 'if' block's condition is not satisfied then the execution breakes out of that block and execute below given 'elif' block, if the given condition is satisfied then the 'grade' variable is initalized and a string value is assigned to it then, it returns the value of 'garde' variable and execution is stopped.
	elif score>=60:
		grade = "Pass"
	# If the above 'elif' block's condition is not satisfied then the execution breakes out of that block and at last execute below given 'else' block and the 'grade' variable is initalized and a string value is assigned to it then, it returns the value of 'garde' variable and execution is stopped.
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail
