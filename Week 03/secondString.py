# Week 03: secondString.py, Weekly Tasks 03
# This program asks the user to input a string
# and outputs every second letter in reverse order
# Author: Ross Downey

x = input("Please enter a string: ") #prompting user to enter string
reversedString = (x [::-1]) #reversing the entire string
every2ndLetterRemoved = (reversedString [1::2]) # starting at 0 index, remove every second letter

print (every2ndLetterRemoved)