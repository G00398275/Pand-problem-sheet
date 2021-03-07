# Weekly task 07, es.py
# This program asks the user to input a text file and outputs the number of e's in this file
# References:
# https://pythonexamples.org/python-re-findall/
# https://www.computerhope.com/issues/ch001721.htm
# A Whirlwind Tour of Python by Jake VanderPlas, Released August 2016, Publisher(s): O'Reilly Media, Inc.
# Author: Ross Downey

import re # importing re module to use re.findall function below

textFile = input ("Please enter the text file to be assessed: ") # Specifying txt file to be inputted

with open(textFile, "rt") as f: # opening inputted txt file
    data = f.read(). strip() # reading and stripping the data in text file

numberofEs = len(re.findall('[eE]', data)) # using re.findall to find all instances of the letter e
# note upper and lowercase e's included

print ('The number of instances of the letter e is {}' .format(numberofEs))