from catan_core.building.building import Building
from catan_core.player.player import Player


class Settlement(Building):
    def __init__(self, player: Player):
        self.player = player
        self.payout = 1
        self.victory_points = 1

    def __eq__(self, o: object) -> bool:
        return self.player == o.player
