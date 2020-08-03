from catan_core.building.building import Building
from catan_core.player.player import Player


class City(Building):
    def __init__(self, player: Player):
        self.player = player
        self.payout = 2
        self.victory_points = 2
