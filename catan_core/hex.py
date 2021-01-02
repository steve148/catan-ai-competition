from typing import List

from catan_core.resource_type.resource_type import ResourceType
from catan_core.vertex import Vertex


class Hex:
    def __init__(self, id: int, resource_type: ResourceType, dice_number: int):
        self.id = id
        self.resource_type = resource_type
        self.dice_number = dice_number
        self.vertices: List[Vertex] = []
        self.robber = False

    def __repr__(self) -> str:
        return f"hex-{self.id}"

    def place_robber(self) -> None:
        self.robber = True

    def remove_robber(self) -> None:
        self.robber = False
