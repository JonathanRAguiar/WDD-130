"""
Aurthor: Wesley Ferreira
Purpose: Write a program that reads from the keyboard the
three numbers for a tire and computes and outputs the volume of space inside that tire.
"""

# Import math method to use math functions
import math
from datetime import datetime, timedelta

today = datetime.now()

#Print a description of this program for the user.
print("This program computes and outputs the volume of space inside of a tire.")
print()

# Define the variables of the formula
w = float(input("Enter the width of the tire in mm (ex 205): ")) # Input the user number as a variable for width
a = float(input("Enter the aspect ratio of the tire (ex 60): ")) # Input the user number for the aspect ratio
d = float(input("Enter the diameter of the wheel in inches (ex 15): ")) # Input the user number for diameter

pi = math.pi # Using the constant PI
exp = math.exp(2) #Using expoent

v = (pi* (w**2) *a*(w*a+2540*d))/10000000000 #Here is the formula

print(f"The approximate volume is {v:.2f} liters") #Output for the user

#print('Current date: ' + str(today.month) + '-' + str(today.day) + '-' + str(today.year))

with open('volumes.txt', 'at') as volumes_file:
    print(f'Current date: {today:%Y-%m-%d}, width: {w}, aspect ratio: {a},diameter: {d}, volume: {v:.2f}', file=volumes_file)
    #2020-03-18, 185, 50, 14, 24.09