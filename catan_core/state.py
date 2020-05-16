import random

resource_types = ["wheat", "wood", "sheep", "clay", "rock"]

from catan_core.development_card.deck import DevelopmentCardDeck


class State:
    """
    Class which stores the state of catan game.
    """

    def __init__(self, players=[]):
        self.players = players
        self.reset()

    def reset(self):
        # There should be 19 of each resource type.
        self.resource_cards = [
            {"type": resource_type, "available": 19} for resource_type in resource_types
        ]

        # Each player gets 15 roads, 5 settlements, and 4 cities.
        self.player_pieces = [
            {"player": player, "roads": 15, "settlements": 5, "cities": 4}
            for player in self.players
        ]

        # Shuffle the development card deck.
        self.development_card_deck = DevelopmentCardDeck()
