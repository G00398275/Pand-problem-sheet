# Week 06: squareRootNewtonMethod.py, Weekly Task 06
# This program inputs a float and outputs an approximation of its square root using the Newton method
# References: https://www.w3schools.com/python/python_functions.asp
# A Whirlwind Tour of Python by Jake VanderPlas, Released August 2016, Publisher(s): O'Reilly Media, Inc.
# Author: Ross Downey

y = 0.001 # Need a point where the function will stop iterating or else will continue indefinitely
# setting to three decimal places is sufficient as result is rounded to one decimal place.

def sqrt(x):
    estimate = 1.0 # Newton's formula requires a starting estimation, set at 1.0 for this
    while True:
        estimate = (estimate + x / estimate) / 2 # Newton formula for square root approximation
        difference = abs(x - estimate ** 2)
        if difference <= y: 
            break # end iteration if the difference becomes less than the "stopPoint"          
    return estimate     # the estimate is returned for subsequent iterations
    
def sqrtApprox():
    while True:
        x = float(input("Please enter a positive floating point number / or enter 0 to quit: "))
        if x == float(0):  
            break # User enters 0 to stop the program  
        print("The square root, acc. to Newton's approximation, is ", round(sqrt(x),1))
        
sqrtApprox() # calling function