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
 # Calculate the LCM.
                            answer = lcm(
                                user1_as_number, user2_as_number, user3_as_number
                            )
                            print(
                                f"The LCM of {user1_as_number}, {user2_as_number} and {user3_as_number} is {answer}"
                            )

# Check if LCM is divisible by two or has a remainder of 1.
                            match answer % 2:
                                case 0:
                                    print(
                                        f"The LCM {answer} of your inputs {user1_as_number, user2_as_number, user3_as_number} is divisible by 2"
                                    )
                                case 1:
                                    print(
                                        f"The LCM {answer} of your inputs {user1_as_number, user2_as_number, user3_as_number} has a remainder of 1"
                                    )
                                case 2:
                                    print("Invalid answer ")

 # Calculates and Displays the first three multiples of the LCM.
                            print("The first three multiples of the LCM is:")
                            for counter in range(1, 4):
                                print(answer * counter)
                            print(" ")
                    else:
                        print("Please enter a positive number")
                else:
                    print("Please enter a positive number")
         


