
def is_digit_check(input):
    if not input.isdigit(): 
        print("Please choose an integer")
        return False
    elif input.isdigit():
        return True
    
def check_in_range(input, x):
    if input not in range(1, x):
        print("Must choose an integer between 1-{}.".format(x-1))
        return False
    else:
        return True    