# Week 05: weekday.py, Weekly Task 05
# This program outputs whether the current day is a weekday or not
# References: https://www.w3schools.com/python/python_datetime.asp
# Author: Ross Downey

import datetime # importing datetime function
today = datetime.datetime.now() # determining what day it is

if (today.strftime("%A")) == "Saturday": # strftime %A gives the current day as a string
     print ("It's the weekend!") 
elif (today.strftime ("%A")) == "Sunday": 
    print ("It's the weekend!") 
else: 
    print ("Unfortunately it's a weekday, get out of bed!") 
# If strftime not equal to "Saturday" or "Sunday", it's a weekday