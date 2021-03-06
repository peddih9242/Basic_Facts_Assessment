import random

def check_rounds():
    while True:
        # ask for amount of rounds
        response = input("How many rounds: ")
        round_error = "Please type either an integer that is higher than 0."
        # if user has not opted for infinite mode, 
        # make input an integer
        if response != "":
            try:
                response = int(response)
                
                # if input is too low, print an error
                if response < 1:
                    print(round_error)
                    continue

            # if input is invalid, print an error
            except ValueError:
                print(round_error)
                continue
        return response

# main routine

rounds = check_rounds()
valid = False
rounds_played = 0
# loop for rounds
while not valid:
    # get numbers to use in question
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    rounds_played += 1
    # round heading
    if rounds == "":
        print("Infinite Mode - Round {}".format(rounds_played))
    else:
        print("Round {} of {}".format(rounds_played, rounds))
    # make question into a string to evaluate
    problem = "{} + {}".format(x, y)
    print(problem)
    # ask for answer
    answer = int(input("Answer: "))
    # check for exit code, rounds met or answer correct/incorrect
    if answer == 12345:
        break
    if rounds_played == rounds:
        valid = True
    elif answer == eval(problem):
        print("Correct!")
    else:
        print("Incorrect.")
print("Thanks for playing")