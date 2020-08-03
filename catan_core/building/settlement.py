from catan_core.player.player import Player
from catan_core.building.building import Building


class Settlement(Building):
    def __init__(self, player: Player):
        self.player = player
        self.payout = 1
        self.victory_points = 1
