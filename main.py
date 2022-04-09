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
# Parameters: A string prompting the user to input a value
# Return values: The user's input converted to a float
# Pre-Conditions: The user input a number
# Post-Conditions: The input has been checked for errors and converted
#                  to a float
#######################################################################

def get_input(message):
    userinput = input(message)

    if userinput.startswith("-"):
        # Input should not be negative. Prompt the user to try again
        print("Please enter a number greater than zero.")
        get_input(message)

    # remove any non-numeric characters from the beginning and end of the string, provided the string is not empty
    while userinput and not userinput[0].isnumeric():
        userinput = userinput[1:]
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
            print("Input must not contain any non-numeric characters other than '/'.")
            get_input(message)

    # something else is wrong. Try again. If or else statement not necessary
    # since a return will prevent this code from running
    print("Input must be either numeric or fractional.")
    get_input(message)


print("")  # message describing what the program does
while True:
    print(get_input("hey write a number: "))

# to fix: negative > positive returns opposite of the negative
#
#         Returns none on the first input after putting alpha characters in middle of string

#         Make sure efficiency not above 100% or 1.0
