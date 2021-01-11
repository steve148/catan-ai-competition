import random
from typing import List

from catan_core.action import Action
from catan_core.board import Board
from catan_core.building.city import City
from catan_core.building.settlement import Settlement
from catan_core.development_card.deck import DevelopmentCardDeck
from catan_core.edge import Edge
from catan_core.player.player import Player
from catan_core.player_hand import PlayerHand
from catan_core.resource_type.clay import Clay
from catan_core.resource_type.deck import ResourceCardDeck
from catan_core.resource_type.rock import Rock
from catan_core.resource_type.sheep import Sheep
from catan_core.resource_type.wheat import Wheat
from catan_core.resource_type.wood import Wood
from catan_core.road import Road
from catan_core.vertex import Vertex


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

        self.dice_rolled = False

        self.player_pieces = {}
        self.bonus_victory_points = {}
        self.player_hand = {}
        for player in self.players:
            # Each player gets 15 roads, 5 settlements, and 4 cities.
            self.player_pieces[player] = {"roads": 15, "settlements": 5, "cities": 4}

            # Bonus victory points
            self.bonus_victory_points[player] = {
                "victory_point_development_cards": 0,
                "longest_road": False,
                "largest_army": False,
            }

            self.player_hand[player] = PlayerHand(player=player)

    def is_game_over(self):
        for player in self.players:
            if self.player_has_won(player=player):
                return player

        return None

    def player_has_won(self, player: Player):
        points = 0

        # Check for any bonus points gained by the player.
        bonus_victory_points = self.bonus_victory_points[player]

        points += bonus_victory_points["victory_point_development_cards"]

        if bonus_victory_points["longest_road"]:
            points += 2

        if bonus_victory_points["largest_army"]:
            points += 2

        # Get the points for the player from pieces on the board.
        points += self.board.victory_points_for_player(player)

        # If the player has reached 10 points, they have won.
        return points >= 10

    def can_build_road(self, player: Player) -> List[Action]:
        if not self.player_hand[player].can_buy_road():
            return []

        return [
            Action(name="build_road", kwargs={"edge": edge})
            for edge in self.board.edges
            if edge.can_place_road(player=player)
        ]

    def can_build_settlement(self, player: Player) -> List[Action]:
        if not self.player_hand[player].can_buy_settlement():
            return []

        return [
            Action(name="build_settlement", kwargs={"vertex": vertex})
            for vertex in self.board.vertices
            if vertex.can_place_building(player=player)
        ]

    def can_build_first_settlement(self, player: Player) -> List[Action]:
        return [
            Action(name="build_first_settlement", kwargs={"vertex": vertex})
            for vertex in self.board.vertices
            if vertex.can_place_starting_building(player=player)
        ]

    def can_build_starting_road(self, player: Player) -> List[Action]:
        return [
            Action(name="build_starting_road", kwargs={"edge": edge})
            for edge in self.board.edges
            if edge.can_place_road(player=player)
        ]

    def can_build_second_settlement(self, player: Player) -> List[Action]:
        return [
            Action(name="build_second_settlement", kwargs={"vertex": vertex})
            for vertex in self.board.vertices
            if vertex.can_place_starting_building(player=player)
        ]

    def player_actions(self, player: Player) -> list:
        actions = []

        # Beginning of turn, force player to roll the dice
        if not self.dice_rolled:
            actions.append(Action(name="roll_dice"))
            return actions

        actions.append(Action(name="end_turn"))

        return actions

    def build_first_settlement(self, player: Player, vertex: Vertex):
        new_settlement = Settlement(player=player)
        vertex.assign_building(new_settlement)

    def build_second_settlement(self, player: Player, vertex: Vertex):
        new_settlement = Settlement(player=player)
        vertex.assign_building(new_settlement)

        for hex in self.board.hexes:
            if vertex in hex.vertices and hex.resource_type:
                self.player_hand[player].add(resource_type=hex.resource_type, count=1)

    def build_starting_road(self, player: Player, edge: Edge):
        new_road = Road(player=player)
        edge.assign_road(road=new_road)

    def build_road(self, player: Player, edge: Edge):
        self.player_hand[player].remove(resource_type=Wood, count=1)
        self.player_hand[player].remove(resource_type=Clay, count=1)
        new_road = Road(player=player)
        edge.assign_road(road=new_road)

    def build_settlement(self, player: Player, vertex: Vertex):
        self.player_hand[player].remove(resource_type=Wood, count=1)
        self.player_hand[player].remove(resource_type=Clay, count=1)
        self.player_hand[player].remove(resource_type=Wheat, count=1)
        self.player_hand[player].remove(resource_type=Sheep, count=1)
        new_settlement = Settlement(player=player)
        vertex.assign_building(building=new_settlement)

    def build_city(self, player: Player, vertex: Vertex):
        self.player_hand[player].remove(resource_type=Rock, count=3)
        self.player_hand[player].remove(resource_type=Wheat, count=2)
        new_city = City(player=player)
        vertex.assign_building(building=new_city)
