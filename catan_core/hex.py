from typing import List

from catan_core.resource_type.resource_type import ResourceType
from catan_core.vertex import Vertex


class Hex:
    def __init__(self, resource_type: ResourceType, number: int):
        self.resource_type = resource_type
        self.number = number
        self.vertices: List[Vertex] = []
        self.robber = False
