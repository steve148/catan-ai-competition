from catan_core.player.player import Player


class Edge:
    def __init__(self):
        self.vertices = []
        self.road = None

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
