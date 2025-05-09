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

