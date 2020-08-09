from catan_core.player.player import Player
from catan_core.road import Road


class Edge:
    def __init__(self):
        self._vertices = []
        self.road = None

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        self._vertices = vertices

    def place_road(self, player: Player) -> None:
        if self.road:
            raise RuntimeError("Edge already has a road placed on it.")

        self.road = Road(player=player)
