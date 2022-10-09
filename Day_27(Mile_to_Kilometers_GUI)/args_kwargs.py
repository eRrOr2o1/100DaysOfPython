# *args: Many Positional Arguments or Positional Variable-Length Arguments
# def add(*args):  # Unlimited Positional Argument
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))

# **kwargs: Many Keyworded Arguments or Keyworded Variable-Length Arguments
# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)

# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")  # If the key is missing then get will return none
#         self.model = kwargs.get("model")
#         self.colour = kwargs.get("colour")
#         self.seats = kwargs.get("seats")
#
#
# my_car = Car(make="Nissan", model="Skyline")
# print(my_car.make)
# print(my_car.model)

