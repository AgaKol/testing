import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.game = CardGame
        self.card1 = Card("ace", 1)
        self.card2 = Card("ten", 10)

    def test_card_is_ace(self):
        self.assertEqual(True, CardGame.check_for_ace(self.game, self.card1))

    def test_card_in_not_ace(self):
        self.assertEqual(False, CardGame.check_for_ace(self.game, self.card2))

    def test_highest_card(self):
        self.assertEqual(self.card2, CardGame.highest_card(self.game, self.card1, self.card2))

    def test_cards_total_value(self):
        cards = [self.card1, self.card2]
        self.assertEqual("You have a total of 11", CardGame.cards_total(self.game, cards))