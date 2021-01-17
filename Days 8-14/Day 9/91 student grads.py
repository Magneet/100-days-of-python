student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score >= 90 :
        student_grades[student] = "Outstanding"
    elif score >=81 and score <=90:
        student_grades[student] = "Exceeds expectations"
    elif score >=71 and score <=80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇
print(student_grades)





