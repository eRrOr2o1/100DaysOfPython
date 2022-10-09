# # Dictionary Comprehension
#
# # Create a new dictionary from a list
# # new_dict = {new_key : new_value for item in list}
# import random
#
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# student_score ={student:random.randint(1, 100) for student in names}
# print(student_score)
#
# print("Passed Students")
#
# # Create a new dictionary from a dictionary
# # new_dict = {new_key:new_value for (key, value) in dict.items() if test}
#
# passed_students = {student:score for (student, score) in student_score.items() if score >= 60}
# print(passed_students)
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame

# for(key, value) in student_data_frame.items():
#     print(value)

# Iterrows
# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    if row.student == "Angela":
        print(row.score)
