import random
import time 

def is_digit_check(input):
    if not input.isdigit(): 
        print("Please choose an integer")
        return False
    elif input.isdigit():
        return 
    
def check_in_range(input, x):
    if input not in range(1, x):
        print("Must choose an integer between 1-{}.".format(x-1))
        return False
    else:
        return     

class Player:
    def __init__(self, name, max_hp=100, flasks = 3, currency=25, current_hp=100, antidote=0, poisoned=0):
        self.name = name 
        self.current_hp = current_hp
        self.max_hp = max_hp
        self._turn_counter = 0
        self.flasks = flasks
        self.currency = currency
        self.antidote = antidote
        self.poisoned = poisoned


    def __str__(self):
        return "\nPlayer : {} | Number of flasks: {} | Current HP: {} | Max HP: {} | antidote: {} | Currency: {} | Poisoned: {}".format(self.name, self.flasks, self.current_hp, self.max_hp, self.antidote, self.currency, "Yes" if self.poisoned > 0 else "No")
    
    def apply_poison(self):
        if self.poisoned > 0: 
            print("Oh no, you are still poisned. Lose 10HP....")
            self.current_hp -= 10
            self.poisoned -= 1
        else:
            return
        
    def get_poisoned(self):
        if self.poisoned == 0:
            print("Oh no you are poisoned, someone must have used a poisonous blade..\nYou will lose 10HP for the next 5 turns")
            self.poisoned = 5
        elif self.poisoned > 0:
            self.poisoned += 5
            print("These bastards. You have been poisoned again. You will lose 10HP for the next {} turns.".format(self.poisoned))

    def use_antidote(self):
        if self.antidote > 0:
            if self.poisoned == 0:
                print("That was a waste... You werent poisoned")
            elif self.poisoned > 0:
                print("EURIKA, YOU ARE CURED OF POISON")
                self.poisoned = 0
                self.antidote -= 1
        elif self.antidote == 0:
            print("You dont have any antidotes....")
            return False


    def use_flask_hp(self):
        """
        ADD FUN PRINT STATEMENTS 
        """
        if self.flasks > 0:
            flask_recover_hp = random.randint(15, 40)
            print("\nHealth flask used to recover HP, you have recovered {} HP".format(flask_recover_hp))
            self.current_hp += flask_recover_hp
            self.current_hp = min(self.current_hp, self.max_hp)
            self.flasks -= 1
        elif self.flasks == 0:
            print("You don't have any flasks...")
            return False


    def use_flask_max_hp(self):
        """
        ADD FUN PRINT STATEMENTS 
        """
        if self.flasks > 0:
            flask_add_max_hp = random.randint(5, 15)
            print("\nHealth Flask used to increase Max HP. Max HP increased by {}".format(flask_add_max_hp))
            self.max_hp += flask_add_max_hp
            self.flasks -= 1
        elif self.flasks == 0:
            print("You don't have any flasks...")
            return False
    
    def do_nothing(self):
        print("\nYou have chosen to do nothing this turn")

    def lose_hp(self):
        """
        ADD FUN PRINT STATEMENTS 
        """
        lost_hp = random.randint(10, 40)
        print("Oh no, you lost {} HP.".format(lost_hp))
        self.current_hp -= lost_hp
    
    def lose_max_hp(self):
        """
        ADD FUN PRINT STATEMENTS 
        """
        lost_max_hp = random.randint(5, 20)
        print("\nOh no, you lost {} max HP".format(lost_max_hp))
        self.max_hp -= lost_max_hp
        self.max_hp = max(self.max_hp, 1)
        self.current_hp = min(self.current_hp, self.max_hp)


    def lose_flask(self):
        """
        ADD FUN PRINT STATEMENTS 
        """ 
        if self.flasks > 0:
            print("You were cornered on the battlefield and one of your flasks were stolen!! \nThieving Bastards...")      
            self.flasks -= 1
        elif self.flasks == 0 and self.currency > 10:
            self.currency -= random.randint(10,25)
            self.currency = max(self.currency, 0)
            print("You were cornered on the battlefield and they demanded one of your flasks.\nYou have no flasks so they've stolen currency instead..")
        elif self.flasks == 0 and self.currency <= 10:
            lost_hp = random.randint(5,20)
            self.current_hp -= lost_hp
            print("Some thieves on the battlefield came to rob you. You had nothing to provide so they beat you up. \nLose {} HP.".format(lost_hp))


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

    def lose_currency(self):
        if self.currency == 0:
            print("You dropped a coin pouch. Luckily your broke so it was empty...")
        elif self.currency > 0:
            lost_money = random.randint(10,30)
            if self.currency > lost_money:
                print("\n Oh no, you dropped one of your pouches. Lose {} currency.".format(lost_money))
                self.currency -= lost_money
            elif lost_money > self.currency:
                partial_lost_money = lost_money - self.currency
                print("\n Oh no, you dropped one of your pouches. Luckily it was only half full. Lose {} currency.".format(partial_lost_money))
                self.currency = 0

class Shop:
    def __init__(self):
        self.inventory = {
            "flasks" : {"Stock": 3, "Price": 50},
            "antidote" : {"Stock": 1, "Price": 75}
        }
    
    def __str__(self):
        return str(self.inventory) 

    def buy_item(self, item, player):
        stock = self.inventory[item]["Stock"]
        price = self.inventory[item]["Price"]
        if player.currency >= price and stock > 0: 
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

    def sell_item(self, item, player):
        player_stock = getattr(player, item)
        price = self.inventory[item]["Price"]
        if player_stock > 0:
            setattr(player, item, getattr(player, item) -1)
            player.currency += price
            self.inventory[item]["Stock"] += 1
        elif player_stock == 0:
            print("You have no {}'s to sell".format(item))
            return False


def print_actions():
        print("\nWhat Would You Like To Do: ")
        print("Use Health Flask to Recover HP?        | enter 1 ")
        print("Use Health Flask to Increase Max HP?   | enter 2 ")
        print("Use Antidote to cure Poison?           | enter 3 ")        
        print("Enter Shop?                            | enter 4 ")
        print("Do nothing ?                           | enter 5 ")

def print_shop():
    print("Please see our current wares below: \n")
    print(shop)
    print("\nType \"1\" to buy flask \nType \"2\" to buy an antidote \nType \"3\" to sell a flask \nType \"4\" to sell an antidote\nType \"5\" to exit shop.")



actions_to_player_options = ["Get Poisoned", "Get Poisoned", "Lose Currency", "Lose Currency", "Lose Currency", "Lose Currency", "Lose HP", "Lose HP", "Lose HP", "Lose HP", "Lose HP", "Lose HP", "Lose Max HP", "Lose Max HP", "Lose Max HP", "Lose Max HP", "Lose Max HP", "Lose Max HP", "Lose Flask", "Lose Flask", "Lose Flask", "Lose Flask", "Nothing Happens", "Gain Flask"]   


def enter_shop(shop_instance, player_instance):
    print("Welcome to the Shop.")
    while True:
        print("Your current currency is: {}".format(player.currency))
        print("You own the following items. Flasks: {}  |  antidotes: {}\n".format(player.flasks, player.antidote))
        print_shop()
        chosen_item = input("\nPlease type here: ")
        if not chosen_item.isdigit(): 
            print("Please choose an integar")
            continue
        chosen_item = int(chosen_item)
        if chosen_item not in range(1,6):
            print("Please choose an integar between 1-5")
            continue
        if chosen_item == 1:
            if shop_instance.buy_item("flasks", player_instance) is False:
                continue
            print("You have just purchased a flask for 50 currency. Returning to shop.....\n")
            time.sleep(1)
            continue
        elif chosen_item == 2:
            if shop_instance.buy_item("antidote", player_instance) is False:
                continue
            print("You have just bought an antidote for 75 currency. Returning to shop.....\n")
            time.sleep(1)
            continue
        elif chosen_item == 3:
            if shop_instance.sell_item("flasks", player_instance) is False:
                continue
            print("You just sold a flask for 50. Returning to shop.....\n")
            time.sleep(1)
            continue
        elif chosen_item == 4:
            if shop_instance.sell_item("antidote", player_instance) is False:
                continue
            print("You just sold an antidote for 75. Returning to shop.....\n")
            time.sleep(1)         
            continue           
        elif chosen_item == 5:
            print("Exiting shop...\n")
            return False
        break


def action_by_player(input, player_instance, shop_instance):
    if input == 1:
        return player_instance.use_flask_hp()
    elif input == 2:
        return player_instance.use_flask_max_hp()
    elif input ==3:
        return player_instance.use_antidote()
    elif input == 4: 
        return enter_shop(shop_instance, player_instance)
    elif input == 5:
        return player_instance.do_nothing()


def action_to_player(instance):
    action = random.choice(actions_to_player_options)
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
    elif action == "Lose Currency":
        instance.lose_currency()
    elif action == "Get Poisoned":
        instance.get_poisoned()


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

if __name__ == '__main__':

    player_name = str(input("Please Type in the name of your character: "))
    player = set_up_player(player_name)

    shop = Shop()
    print("\nWelcome to the game, try and survive for as long as possible without your HP going below zero.... if you can \n")

    while player.current_hp > 0:
        print("New Turn: ")
        print(player)
        while True: 
            print_actions()
            chosen_action = input("\nWhat would you like to choose? : ")
            if is_digit_check(chosen_action) is False:
                continue
            chosen_action= int(chosen_action)
            if chosen_action not in range(1,6):
                print("Please choose an integar between 1-5")
                continue
            if action_by_player(chosen_action, player, shop) is False:
                continue
            break
        if chosen_action in [1,2,3,4]:
            print(player)
        action_to_player(player)
        player._turn_counter += 1 
        player.currency += 10
        player.apply_poison()

    print("Congratulations {}, you have survived {} turns".format(player.name, player._turn_counter))


