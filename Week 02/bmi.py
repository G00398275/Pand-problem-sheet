# Week 02: bmi.py, Weekly Tasks 02
# This program calculates a persons Body Mass Index (BMI)
# Author: Ross Downey

weight = int (input ("Enter your weight (in kg) please:"))# user inputs weight
height = int (input ("Enter your height (in cm) please:"))# user inputs height

BMI = round(weight/((height/100) ** 2), 2) # BMI calculation (converting height to meters)

print("Your BMI is {}".format (BMI)) # Outputs the users BMI