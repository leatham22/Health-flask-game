from shop_class import Shop
from actions import action_by_player, action_to_player
from print_funcs import print_shop, print_actions
from set_up_player import set_up_player
from utils import is_digit_check, check_in_range
from save_highscores import SaveHighScore



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
    with SaveHighScore("highscores.json", player) as highscores:
        print(highscores)

