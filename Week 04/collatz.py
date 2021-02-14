# Week 04: collatz.py, Weekly task
# This program asks the user to input any positive integer
# and outputs the succesive values of the following calculation:
# If even: divide by two
# If odd: multiply by three and add one
# The program stops when the result of the succesive calculations becomes one
# References: https://realpython.com/python-while-loop/
# A Whirlwind Tour of Python by Jake VanderPlas, Released August 2016, Publisher(s): O'Reilly Media, Inc.

# Author: Ross Downey

x = int(input("Enter a positive integer please: "))

while x <= 0:
    print ("That is not a positive integer")
    x = int(input ("Please enter a POSITIVE integer!: "))# Ensuring integer entered is positive

numbers = []
numbers.append(x)
Result = x
# Creating and appending list to be printed at end

while Result != 1: # Initiating while loop, i.e. while x is not equal to 1 loop iterates
    if Result % 2 == 0:
        numbers.append (Result/2)
        Result = Result/2 # if number is even, divide by two and continue
    else:
        numbers.append ((Result * 3) +1)
        Result = Result * 3 + 1 # if number is odd, multiply by three, add one, and continue

for value in numbers: # taken from Lab 4.2.5 
    print (int(value)) # Result outputting as float, converting to integer