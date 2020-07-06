from typing import List

from catan_core.building.building import Building
from catan_core.edge import Edge
from catan_core.port.port import Port


class Vertex:
    def __init__(self, port: Port = None):
        self.edges: List[Edge] = []
        self.port = port
        self.building = None

    def assign_building(self, building: Building):
        if self.building:
            raise RuntimeError("A building already exists at this vertex")

        self.building = building
