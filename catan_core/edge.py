from typing import Optional

from catan_core.player.player import Player
from catan_core.road import Road


class Edge:
    def __init__(self, id: int):
        self.id = id
        self.vertices = []
        self.road: Optional[Road] = None

    def __repr__(self) -> str:
        return f"edge-{self.id}"

    def assign_road(self, road: Road):
        self.road = road

    def can_place_road(self, player: Player) -> bool:
        # return False
        if self.road:
            return False

        for vertex in self.vertices:
            if vertex.building and vertex.building.player == player:
                return True

            if not vertex.building:
                for edge in vertex.edges:
                    if edge != self and edge.road and edge.road.player == player:
                        return True

        return False
