from catan_core.building.building import Building


class City(Building):
    def __init__(self, player):
        self.player = player
        self.payout = 2
        self.victory_points = 2
