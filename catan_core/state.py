import random

from catan_core.board import Board
from catan_core.development_card.deck import DevelopmentCardDeck
from catan_core.resource_card.deck import ResourceCardDeck


class State:
    """
    Class which stores the state of catan game.
    """

    def __init__(self, players=[]):
        # There should be 19 of each resource type.
        self.resource_card_deck = ResourceCardDeck()

        # Shuffle the development card deck.
        self.development_card_deck = DevelopmentCardDeck()

        # Create the board.
        self.board = Board()

        self.players = players.copy()
        random.shuffle(self.players)

        self.current_player_turn = self.players[0]

        # Each player gets 15 roads, 5 settlements, and 4 cities.
        self.player_pieces = {}
        for player in self.players:
            self.player_pieces[player] = {"roads": 15, "settlements": 5, "cities": 4}

        # Bonus victory points
        self.bonus_victory_points = {}
        for player in self.players:
            self.bonus_victory_points[player] = {
                "victory_point_development_cards": 0,
                "longest_road": False,
                "largest_army": False,
            }

    def is_game_over(self):
        for player in self.players:
            if self.player_has_won(player=player):
                return player

        return None

    def player_has_won(self, player):
        points = 0

        bonus_victory_points = self.bonus_victory_points[player]

        points += bonus_victory_points["victory_point_development_cards"]

        if bonus_victory_points["longest_road"]:
            points += 2

        if bonus_victory_points["largest_army"]:
            points += 2

        points += self.board.victory_points_for_player(player)

        return points >= 10
