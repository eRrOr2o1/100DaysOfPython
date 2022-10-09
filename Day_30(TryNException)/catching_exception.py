# FileNotFound Error
# with open("a_file.txt") as file:
#   file.read()

# Key Error
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]
#
# Index Error
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# Type Error
# text = "abc"
# print(text + 5)

# Try/Except/Else/Finally

try:
    file = open("a_file.txt", "w")
except FileNotFoundError as err:
    print(err)
else:
    print("Else")
finally:
    file.close()

# Raise Exception
try:
    file_1 = open("a_file.txt")
except FileNotFoundError as err:
    print(err)
else:
    print("Else")
finally:
    file_1.close()
    raise KeyError("I raised it")