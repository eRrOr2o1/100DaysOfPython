# List Comprehension
# Way 1

# old_list = [1, 2, 3]
# new_list = []
# for n in old_list:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)

# Way 2

# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# name = "Angela"
# new_list = [letter for letter in name]  # separate each letter of a word to a list
# print(new_list)

# Range in list comprehension

# range_list = [num * 2 for num in range(1, 5)]
# print(range_list)

# If in list comprehension
#
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name.upper() for name in names if len(name) > 5]
# print(short_names)
