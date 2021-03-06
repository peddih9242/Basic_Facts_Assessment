import random

# Function(s)
def string_checker(question, valid_list, error):
    # loop function
    valid = False
    while not valid:
        # ask question and make input lowercase
        response = input(question).lower()
        # iterate through list to see if input matches
        # any valid input or first letter of valid input
        for item in valid_list:
            if response == item[0] or response == item:
                return item
        # if input does not match any items in list, print error
        else:
            print(error)

# Main routine
valid = ["addition", "subtraction", "multiplication", "division"]

# loop
a = False
while not a:
    
    # get numbers
    x = random.randint(1, 10)
    y = random.randint(1, 10) 

    # ask if user wants to add, subtract, multiply or divide
    word = string_checker("Do you want to do addition, subtraction, multiplication or division? ", valid, "Please enter addition, subtraction, multiplication or division (or a, s, m or d).")
    if word == "addition":
        print("{} + {}".format(x, y))
    elif word == "subtraction":
        if y > x:
            print("{} - {}".format(y, x))
        else:
            print("{} - {}".format(x, y))
    elif word == "multiplication":
        print("{} * {}".format(x, y))
    elif word == "division":
        numerator = x * y
        if x % 2 == 0:
            print("{} / {}".format(numerator, x))
        else:
            print("{} / {}".format(numerator, y))