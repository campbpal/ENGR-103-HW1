#######################################################################
# Program Filename: ENGR-103-HW1.py
# Author:           Palmer Campbell-Kaswell
# Last updated:     4/8/22
# Description:
# Input:            1. Turbine blade radius
#                   2. Average wind speed
#                   3. Turbine operating efficiency
# Output:           1. Maximum available power
#                   2. Actual power output
#######################################################################

#######################################################################
# Function: get_input
# Description: Retrieves user input and checks for errors. Prompts user
#              to try again if an error occurs
# Parameters: message - a string prompting the user to input a value
#             input_name - a string indicating what variable the user
#                          entered. Used to make error messages input-
#                          specific
# Return values: The user's input converted to a float
# Pre-Conditions: The user input a number
# Post-Conditions: The input has been checked for errors and converted
#                  to a float
#######################################################################
import math


def get_input(message, input_name):
    while True:
        userinput = input(message)

        if userinput.startswith("-"):
            # Input should not be negative. Prompt the user to try again
            # return float(userinput)
            print("Please enter a number greater than zero.")
            continue

        # check that the input starts with a number
        if not userinput[0].isnumeric() and not userinput[0] == ".":
            print(input_name, " must start with a number.")
            continue

        # remove any units from the end of the string, provided the string is not empty
        while userinput and not userinput[-1].isnumeric():
            userinput = userinput[:-1]

        # check if any non-numeric characters remain in the middle of the string
        if userinput.isnumeric():
            return float(userinput)

        # handle fractional inputs. Elif not necessary since this code won't run if the last return happens
        if "/" in userinput and userinput.count("/") == 1:
            # split the string into numerator and denominator
            userinput = userinput.split("/")
            numerator = userinput[0]
            denominator = userinput[1]

            # check whether numerator and denominator are numeric and compute the decimal equivalent
            if numerator.isnumeric() and denominator.isnumeric():
                return float(numerator) / float(denominator)
            else:
                print(input_name, " must be entered as either an integer, a decimal, or a fraction.")
                continue

        # handle decimal inputs
        if "." in userinput and userinput.count(".") == 1:
            try:
                return float(userinput)
            except Exception as e:
                print(e)
                print(input_name, " must be entered as either an integer, a decimal, or a fraction.")
                continue

        # for c in userinput:
        #     unsupported = ""
        #     if not userinput[c].isnumeric() and not userinput[c] in unsupported:
        #         unsupported.append(userinput[c])
        #     if unsupported:
        #         print("The characters ", unsupported)

        # something else is wrong. Try again. If or else statement not necessary
        # since a return will prevent this code from running
        print(input_name, " must be entered as either an integer, a decimal, or a fraction.")
        continue


print("This program calculates the power output of a wind turbine, given its radius, the average wind speed, and the"
      "operating efficiency of the turbine. The density of air is assumed to be 1.2 kg/m^2. All values must be given"
      "as either an integer, a decimal, or a fraction. Scientific notation is not supported at this time. Units do"
      "not need to be included.")

while True:
    radius = get_input("Enter the turbine radius in meters: ", "Turbine radius")
    windspeed = get_input("Enter the average wind speed in meters per second: ", "Wind speed")
    efficiency = get_input("Enter the turbine's operating efficiency as a percent or decimal: ", "Operating efficiency")
    rho = 1.2

    # make sure the efficiency is no greater than 100%
    if efficiency > 100:
        print("Efficiency too high. Please enter a number less than 100%.")
    elif efficiency > 1:
        efficiency = efficiency/100
        print("Efficiency entered as percent. Converted to decimal (", efficiency, ") for calculation")

    area = math.pi * radius ** 2
    maxpower =
