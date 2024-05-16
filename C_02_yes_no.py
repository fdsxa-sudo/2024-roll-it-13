# checks if the user enters yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("you did not choose a valid response")


# main questions
while True:
    want_instructions = yes_no("Do you want to read the instructions?")
    print(f"you chose {want_instructions}")

    roll_again = yes_no("Do yo want to roll again")
    print(f"You said {roll_again}")