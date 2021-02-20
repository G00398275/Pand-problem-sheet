# Week 05: weekday.py, Weekly Task 05
# This program outputs whether the current day is a weekday or not
# References: https://www.w3schools.com/python/python_datetime.asp
# Author: Ross Downey

import datetime # importing datetime function
today = datetime.datetime.now() # determining what day it is

if (today.strftime("%w")) == 0: # strftime %w gives the current day in a number format, 0 = Sunday
     print ("It's the weekend!") 
elif (today.strftime ("%A")) == "Saturday": # strftime %A gives day as a string
    print ("It's the weekend!") 

else: 
    print ("Unfortunately it's a weekday, get out of bed!") 
# If it's not Saturday / Sunday (using strftime functions), it's a weekday.