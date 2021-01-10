from catan_core.player.player import Player


class Road:
    def __init__(self, player: Player):
        self.player = player

    def __eq__(self, o: object) -> bool:
        return self.player == o.player
