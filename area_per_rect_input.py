#!/usr/bin/env python3
# Created By: Liam Csiffary
# Date: April 28, 2021
# this code solves for the area and perimeter
# of a square depending on the information that the user imputs


import math

input_len = int(input("Length of your square = "))
input_wid = int(input("Width of your square = "))
input_unit = input("Units = ")


area = input_len*input_wid

perimeter = (input_len+input_wid)*2

print("\nThe area of a square with a length of {}{}, and a width of {}{} = \
{}{}^2\
".format(input_len, input_unit, input_wid, input_unit, area, input_unit))

print("The perimeter of a square with a length of {}{}, and a width of {}{} = \
{}{}\
".format(input_len, input_unit, input_wid, input_unit, perimeter, input_unit))
