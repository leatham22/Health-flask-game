import random

class Player:
    def __init__(self, name, current_hp=100, max_hp=100):
        self.name = name 
        self.current_hp = current_hp
        self.max_hp = max_hp
        self._turn_counter = 0
        self.flasks = 3

    def __str__(self):
        return "{} | Number of flasks: {} | Starting HP: {} | Max HP: {} ".format(self.name, self.flasks, self.current_hp, self.max_hp)
    
    def use_flask_hp(self):
        """
        ADD FUN PRINT STATEMENTS 
        """
        flask_recover_hp = random.randint(15, 25)
        print("Health flask used to recover HP, you have recovered {} HP".format(flask_recover_hp))
        self.current_hp += flask_recover_hp
        self.flasks -= 1
    
    def use_flask_max_hp(self):
        """
        ADD FUN PRINT STATEMENTS 
        """
        flask_add_max_hp = random.randint(5, 15)
        print("Health Flask used to increase Max HP. Max HP increased by {}".format(flask_add_max_hp))
        self.max_hp += flask_add_max_hp
        self.flasks -= 1

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
        print("Oh no, you lost {} max HP".format(lost_max_hp))
        self.max_hp -= lost_max_hp


    def lose_flask(self):
        """
        ADD FUN PRINT STATEMENTS 
        """ 
        print("You lost a flask on your jouney.")      
        self.flasks -= 1

    def nothing_happens():
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

actions_to_player = ["Lose HP", "Lose HP", "Lose HP", "Lose HP", "Lose Max HP", "Lose Max HP", "Lose Max HP", "Lose Max HP", "Lose Flask", "Lose Flask", "Lose Flask", "Lose Flask", "Nothing Happens", "Gain Flask"]   






