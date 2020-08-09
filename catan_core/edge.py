from catan_core.player.player import Player


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

    def can_place_road(self, player: Player) -> bool:
        if self.road:
            return False

        return True
