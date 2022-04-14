import random
import pandas

numbers = [1, 2, 3]
# new_numbers = [new_item for number in numbers]
new_numbers = [number + 1 for number in numbers]

name = "Patrick"
char_list = [char for char in name]

doubled_range = [number * 2 for number in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
long_names = [name.upper() for name in names if len(name) > 5]

# student_score = {new_key:new_value for item in names}
students_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
# print(students_scores)
# print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
for (index, row) in student_data_frame.iterrows():
    print(row)

# print(student_data_frame)
