import unittest
from main import Player, Shop, set_up_player, action_to_player
from unittest.mock import patch

class TestPlayer(unittest.TestCase):

    def test_use_flask_hp(self):
        player = Player("Test Hero", max_hp=100, current_hp=10)
        player.use_flask_hp()
        self.assertTrue(25 <= player.current_hp <= 50)

    def test_using_flask_reduces_count(self):
        for method in ["use_flask_hp", "use_flask_max_hp"]:
            with self.subTest(flask_method=method):
                player = Player("Hero Test", flasks=3)
                initial_flasks = player.flasks #not needed now but will be useful if flasks amount change for some reason 
                getattr(player, method)()
                self.assertEqual(player.flasks, initial_flasks - 1)

    def test_use_flask_max_hp(self):
        player = Player("Test Hero", max_hp=100)
        player.use_flask_max_hp()
        self.assertTrue(105 <= player.max_hp <= 115)

    def test_use_flask_while_poisoned(self):
        for method in ["use_flask_hp", "use_flask_max_hp"]:
            with self.subTest(flask_method=method):
                player = Player("Test Hero", max_hp=100, flasks=3, current_hp=10, poisoned=5)
                initial_poison = player.poisoned
                getattr(player, method)()
                self.assertEqual(player.poisoned, initial_poison)
                if method == "use_flask_hp":
                    self.assertTrue(25 <= player.current_hp <= 50)
                else:
                    self.assertTrue(105 <= player.max_hp <= 115)

    def test_cure_poison_get_poisoned_sequence(self):
        player = Player("Test Hero", antidote=1, poisoned=15)
        player.use_antidote()
        player.get_poisoned()
        self.assertEqual(player.poisoned, 5)

    def test_no_negative_flasks_hp(self):
        player = Player("Test Hero", current_hp=50, max_hp=100, flasks=0)
        player.use_flask_hp()
        self.assertEqual(player.flasks, 0)
        self.assertEqual(player.current_hp, 50)


    def test_no_negative_flasks__max_hp(self):
        player = Player("Test Hero", flasks=0, max_hp=100)
        player.use_flask_max_hp()
        self.assertEqual(player.flasks, 0)
        self.assertEqual(player.max_hp, 100)
    
    def test_current_hp_not_greater_than_max_hp(self):
        player = Player("Test Hero", current_hp=100, max_hp=100)
        player.use_flask_hp()
        self.assertEqual(player.current_hp, player.max_hp)
    

    def test_lose_flask_above_zero(self):
        player = Player("Test Hero", flasks = 3)
        initial_flasks = player.flasks #not needed now but will be useful if flasks amount change for some reason 
        player.lose_flask()
        self.assertEqual(player.flasks, initial_flasks - 1)

    def test_lose_flask_no_flasks_with_currency(self):
        player = Player("Test Hero", flasks=0, currency=50)
        initial_currency = player.currency
        player.lose_flask()
        self.assertEqual(player.flasks, 0)
        self.assertTrue(player.currency < initial_currency)

    def test_lose_flask_no_flask_no_currency(self):
        player = Player("Test Hero", flasks=0, currency=5, current_hp=100, max_hp=100)
        initial_hp = player.current_hp
        initial_currency = player.currency
        initial_flask = player.flasks
        player.lose_flask()
        self.assertTrue(initial_hp > player.current_hp)
        self.assertEqual(initial_currency, player.currency)
        self.assertEqual(initial_flask, player.flasks)


    def test_lose_hp(self):
        player = Player("Test Hero", current_hp = 100)
        player.lose_hp()
        self.assertTrue(60 <= player.current_hp <= 90)

    def test_lose_max_HP(self):
        player = Player("Test Hero", current_hp=10, max_hp = 100)
        player.lose_max_hp()
        self.assertTrue(80 <= player.max_hp <= 95)

    def test_max_hp_not_below_current_hp(self):
        player = Player("Test Hero", current_hp=100, max_hp = 100)
        player.lose_max_hp()
        self.assertEqual(player.current_hp, player.max_hp)  

    def test_lose_currency_above_zero(self):
        x = [0, 5, 20]
        for money in x:
            with self.subTest(starting_currency=money):
                player = Player("Test Hero", currency=money)
                player.lose_currency()
                self.assertTrue(player.currency >= 0)

    def test_lose_currency(self):
        player = Player("Test Hero", currency=100)
        player.lose_currency()
        self.assertTrue(70 <= player.currency <= 90)

    def test_get_poisoned(self):
        x = [0, 5, 9, 150]
        for poison in x:
            with self.subTest(starting_poisoned=poison):
                player = Player("Test Hero", poisoned=poison)
                player.get_poisoned()
                self.assertEqual(player.poisoned, poison + 5)


    def test_poison_damage_if_poisoned(self):
        player = Player("Test Hero", poisoned=10, current_hp=100, max_hp=100)
        initial_hp = player.current_hp
        player.apply_poison()
        self.assertEqual(player.current_hp, initial_hp - 10)

    def test_poison_damage_if_not_poisoned(self):
        player = Player("Test Hero", poisoned=0, current_hp=100, max_hp=100)
        initial_health = player.current_hp
        player.apply_poison()
        self.assertEqual(player.current_hp, initial_health)

    def test_antidote_cures_poison(self):
        x = [0, 5, 10, 500000000]
        for poison in x:
            with self.subTest(starting_poisoned=poison):
                player = Player("Test Hero", poisoned=poison, antidote=1)
                player.use_antidote()
                self.assertEqual(player.poisoned, 0)

    def test_use_antidote_without_antidote(self):
        player = Player("Test Hero", poisoned=10, antidote=0)
        poisoned_level = player.poisoned
        player.use_antidote()
        self.assertEqual(player.antidote, 0)
        self.assertEqual(player.poisoned, poisoned_level)

class TestShop(unittest.TestCase):
    def test_buy_item_succeeds(self):
        shop = Shop()
        items = ["flasks", "antidote"]
        for item in items: 
            with self.subTest(item_bought = item):
                player = Player("Test Hero", currency = 100)
                starting_currency = player.currency
                starting_item = getattr(player, item)
                shop.buy_item(item, player)
                self.assertEqual(player.currency, starting_currency - shop.inventory[item]["Price"])
                self.assertEqual(starting_item + 1, getattr(player, item))

    def test_buy_item_without_currency(self):
        player = Player("Test Hero", currency=0)
        shop = Shop()
        items = ["flasks", "antidote"]
        for item in items: 
            with self.subTest(attempted_item_bought = item):
                starting_item = getattr(player, item)
                shop.buy_item(item, player)
                self.assertEqual(player.currency, 0)
                self.assertEqual(starting_item, getattr(player, item))


    def test_buy_item_without_stock(self):
        player = Player("Test Hero", currency=100)
        shop = Shop()
        shop.inventory["flasks"]["Stock"] = 0 #emptying shop
        shop.inventory["antidote"]["Stock"] = 0 #emptying shop
        initial_currency = player.currency
        items = ["flasks", "antidote"]
        for item in items: 
            with self.subTest(attempted_item_bought = item):        
                starting_item = getattr(player, item)
                shop.buy_item(item, player)
                self.assertEqual(player.currency, initial_currency)
                self.assertEqual(starting_item, getattr(player, item))                
    
    def test_sell_item_succeeds(self):
        shop = Shop()
        items = ["flasks", "antidote"]
        for item in items: 
            with self.subTest(item_sold = item):
                player = Player("Test Hero", flasks=3, antidote=1, currency = 0)
                starting_item = getattr(player, item)
                shop.sell_item(item, player)
                self.assertEqual(player.currency, shop.inventory[item]["Price"])
                self.assertEqual(starting_item -1, getattr(player, item))        

    def test_sell_without_items(self):
        shop = Shop()
        player = Player("Test Hero", flasks=0, antidote=0, currency=0)
        items = ["flasks", "antidote"]
        for item in items: 
            with self.subTest(attempted_item_sold = item):
                starting_item_stock = getattr(player, item) #stock before trying to sell
                shop.sell_item(item, player)
                self.assertEqual(starting_item_stock, getattr(player, item))
                self.assertEqual(player.currency, 0)


class TestPlayerSetUp(unittest.TestCase):

    @patch('builtins.input')
    def test_no_setup(self, mock_input):
        combo = [("no", 100, 25)]
        for input, expected_hp, expected_currency in combo:
            with self.subTest(input=input):
                mock_input.side_effect = [input]
                player = set_up_player("Test Hero")
                self.assertEqual(player.max_hp, expected_hp)
                self.assertEqual(player.currency, expected_currency)
                self.assertEqual(player.current_hp, player.max_hp)

    @patch('builtins.input')
    def test_correct_inputs(self, mock_input):
        combos = [
            (["yes", "101", "24"], 101, 24),
            (["yes", "75", "50"], 75, 50),
            (["yes", "50", "75"], 50, 75),
        ]
        for input_list, expected_hp, expected_currency in combos:
            with self.subTest(inputted=input_list):
                mock_input.side_effect = list(input_list)
                player = set_up_player("Test Hero")
                self.assertEqual(player.max_hp, expected_hp)
                self.assertEqual(player.currency, expected_currency)
                self.assertEqual(player.current_hp, player.max_hp)

    @patch('builtins.input')        
    def test_incorrect_inputs(self, mock_input):
        mock_input.side_effect = ["maybe", "15", "True", "what", "idk", "yes", "hi", "9999999", "0", "no", "75", "5555555", "0", "20", "75", "50000", "75", "50"]
        player = set_up_player("Test Hero")
        self.assertEqual(player.max_hp, 75)
        self.assertEqual(player.currency, 50)
        self.assertEqual(player.current_hp, player.max_hp)
        self.assertEqual(player.currency + player.max_hp, 125)
        self.assertEqual(player.name, "Test Hero")

class TestActionToPlayer(unittest.TestCase):

    def test_lose_hp(self):
        player = Player("Test Hero", flasks=3, current_hp=100, max_hp=100, currency=50, antidote=1, poisoned=0)
        action_to_player("Lose HP", player)
        self.assertTrue(60 <= player.current_hp <= 90)
        self.assertEqual(player.flasks, 3)
        self.assertEqual(player.max_hp, 100)
        self.assertEqual(player.currency, 50)
        self.assertEqual(player.antidote, 1)
        self.assertEqual(player.poisoned, 0)
        

    def test_lose_max_hp(self):
        player = Player("Test Hero", flasks=3, current_hp=100, max_hp=100, currency=50, antidote=1, poisoned=0)
        action_to_player("Lose Max HP", player)
        self.assertTrue(80 <= player.max_hp <= 95)
        self.assertEqual(player.current_hp, player.max_hp)
        self.assertEqual(player.currency, 50)
        self.assertEqual(player.antidote, 1)
        self.assertEqual(player.poisoned, 0)
        self.assertEqual(player.flasks, 3)
        
    def test_lose_flask(self):
        player = Player("Test Hero", flasks=3, current_hp=100, max_hp=100, currency=50, antidote=1, poisoned=0)
        starting_flasks = player.flasks
        action_to_player("Lose Flask", player)
        self.assertEqual(player.max_hp, 100)
        self.assertEqual(player.current_hp, 100)
        self.assertEqual(player.currency, 50)
        self.assertEqual(player.antidote, 1)
        self.assertEqual(player.poisoned, 0)
        self.assertAlmostEqual(player.flasks, starting_flasks - 1)


    def test_nothing_happens(self):
        player1 = Player("Test Hero", flasks=3, current_hp=100, max_hp=100, currency=50, antidote=1, poisoned=0)
        player2 = Player("Test Hero", flasks=3, current_hp=100, max_hp=100, currency=50, antidote=1, poisoned=0)
        action_to_player("Nothing Happens", player1)
        self.assertEqual(player1.__dict__, player2.__dict__)


    def test_gain_flask(self):
        x = [0, 2, 5, 100000]
        for flask_quantity in x:
            with self.subTest(starting_flask=x):
                player = Player("Test Hero", flasks=flask_quantity, current_hp=100, max_hp=100, currency=50, antidote=1, poisoned=0)
                starting_flasks = player.flasks
                action_to_player("Gain Flask", player)
                self.assertEqual(starting_flasks + 1, player.flasks)
                self.assertEqual(player.max_hp, 100)
                self.assertEqual(player.current_hp, 100)
                self.assertEqual(player.currency, 50)
                self.assertEqual(player.antidote, 1)
                self.assertEqual(player.poisoned, 0)


    def test_lose_currency(self):
        x = [1, 50, 150, 50000]
        for starting_currency in x:
            with self.subTest(currency_loss=starting_currency):
                player = Player("Test Hero", flasks=3, current_hp=100, max_hp=100, currency=starting_currency, antidote=1, poisoned=0)
                initial_currency = player.currency
                action_to_player("Lose Currency", player)
                self.assertTrue(initial_currency > player.currency)
                self.assertEqual(player.antidote, 1)
                self.assertEqual(player.poisoned, 0)
                self.assertEqual(player.max_hp, 100)
                self.assertEqual(player.current_hp, 100)
                self.assertEqual(player.flasks, 3)

    
    def test_get_poisoned(self):
        x = [0, 5, 500]
        for poison in x:
            with self.subTest(starting_poisoned=poison):
                player = Player("Test Hero", flasks=3, current_hp=100, max_hp=100, currency=50, antidote=1, poisoned=poison)
                initial_poison = player.poisoned
                action_to_player("Get Poisoned", player)
                self.assertEqual(initial_poison + 5, player.poisoned)
                self.assertEqual(player.max_hp, 100)
                self.assertEqual(player.current_hp, 100)
                self.assertEqual(player.flasks, 3)
                self.assertEqual(player.currency, 50)
                self.assertEqual(player.antidote, 1)

if __name__ == '__main__':
    unittest.main()
