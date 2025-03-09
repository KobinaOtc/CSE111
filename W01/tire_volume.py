"""
Author: Kobina Otchere
Course: CSE111
"""

# Import Libraries
import math
from datetime import datetime

# Get today's date
today = datetime.now()
date = f"{today:%Y-%m-%d}"

# Get User Input and define pi
pi = math.pi
width = float(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))

# Compute for Volume
volume = ((pi * width**2 * aspect_ratio) * ((width * aspect_ratio) + 2540 * diameter)) / 10000000000

# Print volume
print(f'The approximate volume is {volume:.2f} liters\n')

"""
Exceeding the Requirements
After your program prints the tire volume to the terminal window, your program 
should ask the user if she wants to buy tires with the dimensions that she 
entered. If the user answers “yes”, your program should ask for her phone number
and store her phone number in the volumes.txt file.
"""
make_payment = input('Do you want to purchase tires with the same dimensions: ')
phone_number = ''

if make_payment.lower() == 'yes':
    phone_number = input('\nPlease input your phone number or contact details and an agent will get back to you shortly: ')
    with open('volumes.txt', mode='a') as volumes:
        volumes.write(f"{date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, Client Phone Number: {phone_number}\n")
else:
    with open('volumes.txt', mode='a') as volumes:
        volumes.write(f"{date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")
