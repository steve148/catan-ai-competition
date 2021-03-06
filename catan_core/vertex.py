from typing import List, Optional

from catan_core.building.building import Building
from catan_core.edge import Edge
from catan_core.player.player import Player
from catan_core.port.port import Port


class Vertex:
    def __init__(self, id: int, port: Port = None):
        self.id = id
        self.edges: List[Edge] = []
        self.hexes = []
        self.port = port
        self.building: Optional[Building] = None

    def __repr__(self) -> str:
        return f"vertex-{self.id}"

    def assign_building(self, building: Building):
        if self.building:
            raise RuntimeError("A building already exists at this vertex")

        self.building = building

    def can_place_building(self, player: Player) -> bool:
        if all(not edge.road or edge.road.player != player for edge in self.edges):
            return False

        return self.can_place_starting_building(player=player)

    def can_place_starting_building(self, player: Player) -> bool:
        if self.building:
            return False

        # Buildings must be at least 2 edges apart.
        for edge in self.edges:
            for vertex in edge.vertices:
                if vertex.building:
                    return False

        return True
