import random

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
        self.resource_cards = [
            {"type": resource_type, "available": 19} for resource_type in resource_types
        ]

        # Each player gets 15 roads, 5 settlements, and 4 cities.
        self.player_pieces = [
            {"player": player, "roads": 15, "settlements": 5, "cities": 4}
            for player in self.players
        ]

        # Shuffle the development card deck.
        knight_cards = [{"type": "knight"} for i in range(14)]
        monopoly_cards = [{"type": "monopoly"} for i in range(2)]
        road_building_cards = [{"type": "road_building"} for i in range(2)]
        year_of_plenty_cards = [{"type": "year_of_plenty"} for i in range(2)]
        victory_point_cards = [{"type": "victory"} for i in range(5)]
        self.development_cards = (
            knight_cards
            + monopoly_cards
            + road_building_cards
            + year_of_plenty_cards
            + victory_point_cards
        )
        random.shuffle(self.development_cards)
