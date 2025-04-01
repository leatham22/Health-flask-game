import random

class Player:
    def __init__(self, name, max_hp=100, currency=25, current_hp=100, antidote=0):
        self.name = name 
        self.current_hp = current_hp
        self.max_hp = max_hp
        self._turn_counter = 0
        self.flasks = 3
        self.currency = currency
        self.antidote = antidote


    def __str__(self):
        return "\nPlayer : {} | Number of flasks: {} | Current HP: {} | Max HP: {} | Currency: {} ".format(self.name, self.flasks, self.current_hp, self.max_hp, self.currency)
    
    def use_flask_hp(self):
        """
        ADD FUN PRINT STATEMENTS 
        """
        flask_recover_hp = random.randint(15, 25)
        print("\nHealth flask used to recover HP, you have recovered {} HP".format(flask_recover_hp))
        self.current_hp += flask_recover_hp
        self.current_hp = min(self.current_hp, self.max_hp)
        self.flasks -= 1
    
    def use_flask_max_hp(self):
        """
        ADD FUN PRINT STATEMENTS 
        """
        flask_add_max_hp = random.randint(5, 15)
        print("\nHealth Flask used to increase Max HP. Max HP increased by {}".format(flask_add_max_hp))
        self.max_hp += flask_add_max_hp
        self.flasks -= 1
    
    def do_nothing(self):
        print("\nYou have chosen to do nothing this turn")

    def lose_hp(self):
        """
        ADD FUN PRINT STATEMENTS 
        """
        lost_hp = random.randint(5, 25)
        print("Oh no, you lost {} HP.".format(lost_hp))
        self.current_hp -= lost_hp
    
    def lose_max_hp(self):
        """
        ADD FUN PRINT STATEMENTS 
        """
        lost_max_hp = random.randint(1, 15)
        print("\nOh no, you lost {} max HP".format(lost_max_hp))
        self.max_hp -= lost_max_hp
        self.max_hp = max(self.max_hp, 1)
        self.current_hp = min(self.current_hp, self.max_hp)


    def lose_flask(self):
        """
        ADD FUN PRINT STATEMENTS 
        """ 
        print("You lost a flask on your jouney.")      
        self.flasks -= 1

    def nothing_happens(self):
        """
        ADD FUN PRINT STATEMENTS 
        """
        print("You survived the battle with no wounds. Congratulations, no changes.")
    
    def gain_flask(self):
        """
        ADD FUN PRINT STATEMENTS 
        """      
        print("You picked up a flask of a fallen comrade, flasks increased by 1. ")  
        self.flasks += 1

class Shop:
    def __init__(self):
        self.inventory = {
            "flasks" : {"Stock": 2, "Price": 50},
            "antidote" : {"Stock": 1, "Price": 75}
        }
    
    def __str__(self):
        return str(self.inventory) 

    def buy_item(self, item, player):
        stock = self.inventory[item]["Stock"]
        price = self.inventory[item]["Price"]
        if player.currency > price and stock > 0: 
            self.inventory[item]["Stock"] -= 1
            setattr(player, item, getattr(player, item) + 1) #used so method is dynamic
            player.currency -= self.inventory[item]["Price"]
        elif player.currency >= price and stock == 0:
            print("The item is out of stock. Lets try again.")
            return False
        elif player.currency < price and stock > 0:
            print("You have insufficient funds. Lets Try again.")
            return False
        elif player.currency < price and stock == 0:
            print("The Item is out of stock and you have insufficient funds. Lets try again.")
            return False
    """
    def buy_lucky_charm(self, player):
        
        Add Charm that halves the max hp lost.
        
        return
    """
def print_actions():
        print("\nWhat Would You Like To Do: ")
        print("Use Health Flask to Recover HP?        | enter 1 ")
        print("Use Health Flask to Increase Max HP?   | enter 2 ")
        print("Enter Shop?                            | enter 3 ")
        print("Do nothing ?                           | enter 4 ")

def print_shop():
    print("Welcome to the shop, please see our wares below: \n")
    print(shop)
    print("\nType \"1\" to buy flask | Type \"2\" to buy an antidote | Type \"3\" to exit without purchasing.")

def choose_random_action_on_player(instance):
    if instance.flasks < 1: 
        action= random.choice(zero_flask_actions_to_player_options)
    else: 
        action = random.choice(actions_to_player_options)
    return action

actions_to_player_options = ["Lose HP", "Lose HP", "Lose HP", "Lose HP", "Lose Max HP", "Lose Max HP", "Lose Max HP", "Lose Max HP", "Lose Flask", "Lose Flask", "Lose Flask", "Lose Flask", "Nothing Happens", "Gain Flask"]   
zero_flask_actions_to_player_options = ["Lose HP", "Lose HP", "Lose HP", "Lose HP", "Lose Max HP", "Lose Max HP", "Lose Max HP", "Lose Max HP", "Nothing Happens", "Gain Flask"]   

def enter_shop(shop_instance, player_instance):
    print_shop()
    while True:
        chosen_item = input("\nPlease type here: ")
        if not chosen_item.isdigit(): 
            print("Please choose an integar")
            continue
        chosen_item = int(chosen_item)
        if chosen_item not in range(1,4):
            print("Please choose an integar between 1-3")
            continue
        if chosen_item == 1:
            if shop_instance.buy_item("flasks", player_instance) is False:
                print_shop()
                continue
            print("You have just purchased a flask for 50 currency")
        elif chosen_item == 2:
            if shop_instance.buy_item("antidote", player_instance) is False:
                print_shop()
                continue
            print("You have just bought an antidote for 75 currency")
        elif chosen_item == 3:
            print("Exiting shop...\nThe Shop Keeper is not happy.")
            return False
        break


def action_by_player(input, player_instance, shop_instance):
    if input == 1:
        return player_instance.use_flask_hp()
    elif input == 2:
        return player_instance.use_flask_max_hp()
    elif input == 3: 
        return enter_shop(shop_instance, player_instance)
    elif input == 4:
        return player_instance.do_nothing()


def action_to_player(action, instance):
    if action == "Lose HP":
        instance.lose_hp()
    elif action == "Lose Max HP":
        instance.lose_max_hp() 
    elif action == "Lose Flask":
        instance.lose_flask() 
    elif action == "Nothing Happens":
        instance.nothing_happens() 
    elif action == "Gain Flask":
        instance.gain_flask() 





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
                if not starting_max_hp.isdigit():
                    print("Please choose an integar")
                    continue
                starting_max_hp = int(starting_max_hp)
                if starting_max_hp not in range(1, 126):
                    print("Must choose integer between 1-125.")
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
                    if starting_curency not in range(1, 125):
                        print("Must choose integer between 1-124 (as max HP cannot be zero)")
                        continue
                    if not starting_curency + starting_max_hp == 125:
                        print("God your maths is terrible. The total of both must be equal to 125.")
                        continue
                    player = Player(player_name, starting_max_hp, starting_curency)
                    return player

player_name = str(input("Please Type in the name of your character: "))
player = set_up_player(player_name)


shop = Shop()
print("\nWelcome to the game, try and survive for as long as possible without your HP going below zero.... if you can \n")

while player.current_hp > 0:
    print(player)
    if player.flasks < 1 and player.currency < 50: 
        print("\nRun out of flasks..! Only option is to do nothing....")
        chosen_action = 3
    else: 
        while True: 
            print_actions()
            chosen_action = input("\nWhat would you like to choose? : ")
            if not chosen_action.isdigit(): 
                print("Please choose an integar")
                continue
            chosen_action= int(chosen_action)
            if chosen_action not in range(1,5):
                print("Please choose an integar between 1-4")
                continue
            if action_by_player(chosen_action, player, shop) is False:
                continue
            break
    if chosen_action in [1,2,4]:
        print(player)
    action_on_player = choose_random_action_on_player(player)
    action_to_player(action_on_player, player)
    player._turn_counter += 1 
    player.currency += 10

print("Congratulations {}, you have survived {} turns".format(player.name, player._turn_counter))


