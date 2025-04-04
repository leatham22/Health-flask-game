from print_funcs import print_shop
import time


def enter_shop(shop_instance, player_instance):
    print("Welcome to the Shop.")
    while True:
        print("Your current currency is: {}".format(player_instance.currency))
        print("You own the following items. Flasks: {}  |  antidotes: {}\n".format(player_instance.flasks, player_instance.antidote))
        print_shop(shop_instance)
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

