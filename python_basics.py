# clears the screen
import os
import namer_module

os.system("clear")

# Variables
first_name = "John"
age = 45

print(first_name, age)
first_name = "Bob-O"
age = 65
print(first_name, age)

"""
#DATA TYPES
strings - "Pizza"
numbers - floats(decimals) & Ints
booleans true/false
lists- ["A", "B", "C"]immutable-you can change/update
tuples-("A", "B, "C")unchangeable. faster processing times
dictionaries- fav_pizza = {"John":"Pepperoni"} key value pairs 
"""
# \t adds a tab to the line of code and
# \n add a new line to the code following
# adding an f right before a string adds the ability to add in a variable with {}.
mom = "AnGelA"
yell = f'My mom {mom} yelled: \n"Clean your room!"'
print(yell)

# .upper added to a variable will uppercase letters same with .lower
# .title will capitalize every word. .capitalize will uppercase the 1st word.
# len(variable) will give you the numbers of characters including spaces
print(
    mom[0:3]
)  # this will print only certain characters of a variable in this case 1st thru 4th.
print(mom.capitalize())
print(mom.upper())
print(mom.swapcase())

num_1 = 5.25
num_2 = 3.7253
num_3 = 5
print(num_1 + num_2)
# above results in a float. if you add int() it rounds it to make it an integer.
print(int(num_1 + num_2))
# inversely, you can make an int a float with float()
print(float(num_3))
# you can round to a specific place
print(round(num_2, 2))


# LISTS

# You can put lists in lists and pull out specific entries
nums = [1, 2, 3, 4, 5]
things = ["Anita", "Pyramid", nums]
# since the 2th space is a list of numbers, you can then add to that number for example:
print(things)
print(things[2][1] + 10)

# replace things in list by assigning the -th
things[0] = "John"
print(things)

# If you want to add things to end of list add "append"
things.append("Anita")
print(things)

# DELETE with del()
del things[3]
print(things)

# TUPLES (probably wont use these much)
# same as lists but with () instead of []. They are unchanegable but you can combine them to create a new tuple
tuple_1 = (0, 1, 2)
tuple_2 = (3, 4, 5)
tuple_3 = tuple_1 + tuple_2
print(tuple_3)

# to print a selection of a tuple the : is used as a "through" which wont return the 2th just up to the 2th.
print(tuple_3[0:2])


# DICTIONARIES
best_za = {"lous": "deep dish", "jets": "sicilian", "the hut": "stuffed crust"}
print(best_za)
print(best_za["lous"])


# COMPARISON OPERATORS
print(10 == 10)
print(9 == 10)
print(9 != 10)
print(9 <= 10)
print(1 > 100)
print((1 + 10) == 11)


# CONDITIONAL STATEMENTS

# if elif else
num = 5
if num > 10:
    print("Your numbers is greater than 10")
elif num == 10:
    print("Your number is equal to 10")
else:
    print("Your number is NOT greater than 10")

# AND / OR condition multiplier allows you to test two or more different things that must be all true in order to return true.
if (num > 10) and (num < 100):
    print("Your numbers is greater than 10")
else:
    print("NOPE")

# WHILE LOOPS
counter = 0
while counter <= 5:
    print(f"Count is {counter}")
    counter += 1

# FOR lOOPS
names = "Horatio", "Edgar", "Felipe"
for name in names:
    print(name)

for key, value in best_za.items():
    print(key)


# def stands for define. you throw that in front of the function name
def name(first_name):
    print(f"Hey there {first_name}")


# after you define it, you can call the function:
name("John")


# Simple Number Function example
def divider(num1, num2):
    print(int(num1 / num2))


divider(100, 10)


# Using "return" in functions
def namer(first_name):
    count = 0
    for letter in first_name:
        count += 1
    return count


# Call the function
letter_count = namer("Penelope")
print(f"There are {letter_count} letters in this name")


# Used an import module from a separate file which included the function "namer". Saved in same directory
print(namer_module.namer("Danny"))

# Classes


class Square:
    # almost always pass self as the first argument in classes. Then we define the squares side length
    def __init__(self, side_length):
        self.side_length = side_length

    # Get area of square by calling a method using def and self
    def area(self):
        return self.side_length * self.side_length

    # get perimeter
    def perimeter(self):
        return self.side_length * 4

    # create a report
    def report(self):
        print(f"The side length of this square using classes is {self.side_length}.\n")
        print(f"The area of this square using classes is {self.area()}.\n")
        print(f"The perimeter of this square using classes is {self.perimeter()}")


# initiate our class
my_square = Square(5)

# call the class methods(functions)
print(my_square.side_length)
print(my_square.area())
print(my_square.perimeter())
my_square.report()
