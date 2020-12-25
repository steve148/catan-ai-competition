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
        # return False
        if self.road:
            return False

        for vertex in self.vertices:
            if not vertex.building or vertex.building.player == player:
                for edge in vertex.edges:
                    if edge != self and edge.road and edge.road.player == player:
                        return True

        return False
