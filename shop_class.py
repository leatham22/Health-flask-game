
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