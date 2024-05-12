print("🎲🎲 Roll it 13🎲🎲")

# Loop for testing purposes

while True:
    want_instructions = input("Do you want to read the instructions? ").lower()
    if want_instructions == "yes":
        print(f"You chose {want_instructions}")
    elif want_instructions == "no":
        print(f"You chose {want_instructions}")
    elif want_instructions == "y":
        print(f"You chose yes")
    elif want_instructions == "n":
        print(f"You chose no")
    else:
        print("You did not choose a valid answer.")
