import random


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