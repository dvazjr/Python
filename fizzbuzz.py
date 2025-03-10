# clears the screen
import os

os.system("clear")

# FIZZBUZZ
# print 1-100 If divisible by 3 label "fizz" If divis by 5 label "buzz" Finally if divis by 3&5  label "fizzbuzz" otherwise just print the number
count = 1
while count <= 100:
    if (count % 3 == 0) and (count % 5 == 0):
        print(f"{count}. FizzBuzz!")
    elif count % 3 == 0:
        print(f"{count}. Fizz")
    elif count % 5 == 0:
        print(f"{count}. Buzz")
    else:
        print(f"{count}.")

    count += 1  # One mistake I made was didn't indent. If you dont indent, it wont be "inside" the loop. Different than JavaScript.
