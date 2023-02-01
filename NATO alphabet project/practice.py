import random as r

# list comprehension
numbers = [1, 2, 3, 4, 5, 6]
new_numbers = [1 + n for n in numbers]
print(new_numbers)

name = "michael"
letter_list = [letter for letter in name]
print(letter_list)

new_range = [n*2 for n in range(1, 5)] # [1, 2, 3, 4]
print(new_range)

names = ["Katara", "Toph", "Aang", "Zuko", "Sokka"]
short_names = [name for name in names if len(name)<5]
print(short_names)

names = ["Katara", "Toph", "Aang", "Zuko", "Sokka"]
upper_names = [name.upper() for name in names if len(name)>4]
print(upper_names)

# dict comprehension
names = ["Katara", "Toph", "Aang", "Zuko", "Sokka"]

students_scores ={
    student:r.randint(1,100) for student in names
}
print(students_scores)

passed_students = {
    student:score for (student, score) in students_scores.items() if score >= 50
}
print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}