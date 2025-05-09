#!/usr/bin/env python3

# Created By: Amara Tie

# Date: April 29, 2025

# This is a program calculates the LCM of 3 numbers!

def lcm(number_1, number_2, number_3):
    counter = 1
    while True:
        counter += 1
        if (
            counter % number_1 == 0
            and counter % number_2 == 0
            and counter % number_3 == 0
        ):
            return counter

def main():


    # Greeting.
    print("Hello! Let's find the LCM, remainder and multiples of 3 numbers!")

    # Ask User for a number.
    user1_as_string = input("Enter the first number :")
    user2_as_string = input("Enter a second number :")
    user3_as_string = input("Enter a third number :")
    print("")

    # Try to convert a string to int.
    try:
        user1_as_number = round(float(user1_as_string))
        try:
            user2_as_number = round(float(user2_as_string))
            try:
                user3_as_number = round(float(user3_as_string))

# Check if the number is positive.
                if user1_as_number > 0:
                    if user2_as_number > 0 and user3_as_number > 0:
                        if user2_as_number > 0 and user3_as_number > 0:




