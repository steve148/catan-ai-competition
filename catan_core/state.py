import random

from catan_core.development_card.deck import DevelopmentCardDeck
from catan_core.resource_card.deck import ResourceCardDeck

resource_types = ["wheat", "wood", "sheep", "clay", "rock"]


class State:
    """
    Class which stores the state of catan game.
    """

    def __init__(self, players=[]):
        self.players = players
        self.reset()

    def reset(self):
        # There should be 19 of each resource type.
        self.resource_card_deck = ResourceCardDeck()

        # Each player gets 15 roads, 5 settlements, and 4 cities.
        self.player_pieces = [
            {"player": player, "roads": 15, "settlements": 5, "cities": 4}
            for player in self.players
        ]

        # Shuffle the development card deck.
        self.development_card_deck = DevelopmentCardDeck()
