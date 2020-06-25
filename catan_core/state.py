from catan_core.board import Board
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

        # Shuffle the development card deck.
        self.development_card_deck = DevelopmentCardDeck()

        # Create the board.
        # TODO: need to implement board class first.
        self.board = None

        # Each player gets 15 roads, 5 settlements, and 4 cities.
        self.player_pieces = [
            {"player": player, "roads": 15, "settlements": 5, "cities": 4}
            for player in self.players
        ]

        # Bonus victory points
        self.bonus_victory_points = [
            {
                "player": player,
                "victory_point_development_cards": 0,
                "longest_road": False,
                "largest_army": False,
            }
            for player in self.players
        ]
