from player_class import Player
from utils import is_digit_check, check_in_range

def set_up_player(name):    
    while True:
        customisation = input("Would you like to customise your starting stats? Answer \"yes\" or \"no\": ").lower()
        if customisation not in ["yes", "no"]:
            print("Please choose a valid answer \"yes\" or \"no\"")
            continue 
        if customisation == "no":
            player = Player(name)
            return player
        if customisation == "yes":
            print("Here are the rules:\n1. You can edit your starting Max HP and Currency.\n2. The Sum of the two must be equal to 125.\n3. Your Starting HP will match your chosen Max HP")
            while True: 
                starting_max_hp = input("Please choose your starting Max HP: ")
                if is_digit_check(starting_max_hp)is False:
                    continue
                starting_max_hp = int(starting_max_hp)
                if check_in_range(starting_max_hp, 126) is False:
                    continue 
                if starting_max_hp == 125:
                    player = Player(name, starting_max_hp, 0)
                    return player
                else:
                    starting_curency = input("Please choose your starting currency: ")
                    if not starting_curency.isdigit():
                        print("Please choose an integar")
                        continue
                    starting_curency = int(starting_curency)
                    if check_in_range(starting_curency, 125) is False:
                        continue
                    if not starting_curency + starting_max_hp == 125:
                        print("God your maths is terrible. The total of both must be equal to 125.")
                        continue
                    player = Player(name, max_hp=starting_max_hp, currency=starting_curency, current_hp=starting_max_hp)
                    return player