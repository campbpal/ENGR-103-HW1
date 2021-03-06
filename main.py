#######################################################################
# Program Filename: ENGR-103-HW1.py
# Author:           Palmer Campbell-Kaswell
# Last updated:     4/8/22
# Description:      This program calculates the power output of a wind
#                   turbine, given its radius, the average wind speed,
#                   and the operating efficiency of the turbine. It
#                   then estimates how many turbines would be required
#                   to power one person's life in Oregon.
# Input:            1. Turbine blade radius
#                   2. Average wind speed
#                   3. Turbine operating efficiency
#                   4. Would the user like to run the program again?
# Output:           1. Maximum available power
#                   2. Actual power output
#                   3. The number of turbines required to power one
#                      person's life for a year in Oregon
#######################################################################

import math

JOULES_PER_CAPITA_OR = 2.57e10
YEARS_PER_SECOND = 1 / (60 * 60 * 24 * 365)

#######################################################################
# Function name:    get_numeric_input
# Description:      Retrieves numeric input and checks for errors.
#                   Prompts user to try again if an error occurs.
# Parameters:       message - a string prompting the user to input a
#                             value
#                   input_name - a string indicating what variable the
#                                user entered. Used to make error
#                                messages input-specific.
# Return values:    The user's input converted to a float
# Pre-Conditions:   The user input a number
# Post-Conditions:  The input has been checked for errors and converted
#                   to a float.
#######################################################################


def get_numeric_input(message, input_name):
    while True:
        user_input = input(message)

        if user_input.startswith("-"):
            # Input should not be negative. Prompt the user to try again
            print("Please enter a number greater than zero.")
            continue

        # check that the input starts with a number
        if not user_input[0].isnumeric() and not user_input[0] == ".":
            print(input_name, "must start with a number.")
            continue

        # remove any units from the end of the string, provided the string is not empty
        while user_input and not user_input[-1].isnumeric():
            user_input = user_input[:-1]

        # check if any non-numeric characters remain in the middle of the string
        if user_input.isnumeric():
            if float(user_input) > 0:
                return float(user_input)
            print("Please enter a number greater than zero.")
            continue

        # handle fractional inputs. Elif not necessary since this code won't run if the last return happens
        if "/" in user_input and user_input.count("/") == 1:
            # split the string into numerator and denominator
            user_input = user_input.split("/")
            numerator = user_input[0]
            denominator = user_input[1]

            # check whether numerator and denominator are numeric and greater than zero,
            # and compute the decimal equivalent
            if numerator.isnumeric() and denominator.isnumeric():
                if float(numerator) <= 0:
                    print("Please enter a number greater than zero.")
                    continue
                if float(denominator) <= 0:
                    print("Divide by zero not supported.")
                    continue
                return float(numerator) / float(denominator)
            else:
                print(input_name, "must be entered as either an integer, a decimal, or a fraction.")
                continue

        # handle decimal inputs
        if "." in user_input and user_input.count(".") == 1:
            try:
                # make sure the input is greater than zero
                if float(user_input) > 0:
                    return float(user_input)
                print("Please enter a number greater than zero.")
                continue
            except Exception as e:
                print(e)
                print(input_name, "must be entered as either an integer, a decimal, or a fraction.")
                continue

        # something else is wrong, try again
        print(input_name, "must be entered as either an integer, a decimal, or a fraction.")
        continue


print("\nThis program calculates the power output of a wind turbine, given its radius, the average wind speed, and the"
      "\noperating efficiency of the turbine. It then estimates how many turbines would be required to power one\n"
      "person's life in Oregon. The density of air is assumed to be 1.2 kg/m\u00b2. All values must be given as "
      "either\nan integer, a decimal, or a fraction. Scientific notation is not supported at this time. "
      "Units do not need \nto be included. \n")

while True:
    rho = 1.2
    radius = get_numeric_input("Enter the turbine radius in meters: ", "Turbine radius")
    windspeed = get_numeric_input("Enter the average wind speed in meters per second: ", "Wind speed")

    while True:
        efficiency = get_numeric_input("Enter the turbine's operating efficiency as a percent or decimal: ",
                                       "Operating efficiency")

        # make sure the efficiency is no greater than 100%. Convert to decimal if above 1.0
        if efficiency > 100:
            print("\nEfficiency too high. Please enter a number less than 100%.")
            continue
        elif efficiency > 1:
            efficiency = efficiency/100
            print("\nEfficiency entered as percent. Converted to decimal (" + str(efficiency) + ") for calculation.")
            break
        else:
            break

    # calculate results
    area = math.pi * radius ** 2
    max_power = 0.5 * rho * area * windspeed ** 3
    actual_power = efficiency * max_power
    num_turbines_per_person_OR = JOULES_PER_CAPITA_OR * (1 / actual_power) * YEARS_PER_SECOND

    # output results to the user
    print("\nTurbine area: ", round(area, 2), "m\u00b2")
    print("Maximum available power:", round(max_power, 2), "W")
    print("Actual power output:", round(actual_power, 2), "W")
    print("\n")
    print("In 2019, the average Oregonian used roughly 2.58x10\u00b9\u2070 Joules of electricity. Given these "
          "parameters, it\nwould take about", round(num_turbines_per_person_OR, 2), "wind turbines to produce enough "
                                                                                    "electricity for one person.\n")

    # ask the user if they would like to run the program again
    while True:
        repeat = input("Run the program again? (yes or no) ")
        if repeat.lower() == "yes":
            print("")
            break
        elif repeat.lower() == "no":
            break
        else:
            print("Please enter either yes or no.")
            continue
    if repeat.lower() == "no":
        break
