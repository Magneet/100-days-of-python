import pandas
student_dict ={
    "student": ["Miep", "Wouter", "Henk"],
    "score": [56,76,23]
}

student_panda_fram = pandas.DataFrame(student_dict)
for (index, row) in student_panda_fram.iterrows():
    print(row.student)
