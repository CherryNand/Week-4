# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) #changed str to int and added an extra bracket

exam_three = int(input("Input exam grade three: ")) #changed exam_3 to exam_three and added int

grades = [exam_one, exam_two, exam_three] #added commas
sum = 0
for grade in grades: #changed "grade" to "grades"
  sum = sum + grade

avg = sum / len(grades)#changed "grdes" to "grades"

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #colon
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = 'C' #changed "C' to 'C'
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else: #changed elif to else
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade=="F": #changed is to =="
    print ("Student is failing.") #added paranthesis
else:
    print ("Student is passing.") #added paranthesis
