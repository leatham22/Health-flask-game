import random
from shop_actions import enter_shop

actions_to_player_options = ["Get Poisoned", "Get Poisoned", "Lose Currency", "Lose Currency", "Lose Currency", "Lose Currency", "Lose HP", "Lose HP", "Lose HP", "Lose HP", "Lose HP", "Lose HP", "Lose Max HP", "Lose Max HP", "Lose Max HP", "Lose Max HP", "Lose Max HP", "Lose Max HP", "Lose Flask", "Lose Flask", "Lose Flask", "Lose Flask", "Nothing Happens", "Gain Flask"]


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