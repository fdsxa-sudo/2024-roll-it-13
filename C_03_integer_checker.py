
# checks that users enter an integer
# that is more than 13
def int_check():

    while True:
    
        error = "please enter integer that is 13 or more"
    
    
        try:
            response = int(input("enter an integer: "))
    
            # checks that the number is more than / equal to 13
            if response < 13:
                print(error)
            else:
                print("your number is ", response)
    
        except ValueError:
            print(error)

# main routine goes here
target_score = int_check()
print(target_score)