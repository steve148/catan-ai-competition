from typing import Type

from catan_core.player.player import Player
from catan_core.resource_type.clay import Clay
from catan_core.resource_type.resource_type import ResourceType
from catan_core.resource_type.rock import Rock
from catan_core.resource_type.sheep import Sheep
from catan_core.resource_type.wheat import Wheat
from catan_core.resource_type.wood import Wood


class PlayerHand:
    def __init__(self, player: Player):
        self.player = player
        self.hand = {}
        for resource_type in [Clay, Rock, Sheep, Wheat, Wood]:
            self.hand[resource_type] = 0

    def __eq__(self, o: object) -> bool:
        if self.player != o.player:
            return False

        for resource_type in [Clay, Rock, Sheep, Wheat, Wood]:
            if self.hand[resource_type] != o.hand[resource_type]:
                return False

        return True

    def has(self, resource_type: Type[ResourceType], count: int) -> bool:
        return self.hand[resource_type] >= count

    def add(self, resource_type: Type[ResourceType], count: int) -> None:
        if not count > 0:
            raise RuntimeError("Cannot add 0 or less cards to the hand.")

        self.hand[resource_type] += count

    def remove(self, resource_type: Type[ResourceType], count: int) -> int:
        if not count > 0:
            raise RuntimeError("Cannot remove 0 or less cards from the hand.")

        if self.hand[resource_type] < count:
            count_removed = self.hand[resource_type]
            self.hand[resource_type] = 0
            return count_removed
        else:
            self.hand[resource_type] -= count
            return count

    def can_buy_road(self):
        return self.has(resource_type=Wood, count=1) and self.has(
            resource_type=Clay, count=1
        )

    def can_buy_settlement(self):
        return (
            self.has(resource_type=Wood, count=1)
            and self.has(resource_type=Clay, count=1)
            and self.has(resource_type=Wheat, count=1)
            and self.has(resource_type=Sheep, count=1)
        )

    def can_buy_city(self):
        return self.has(resource_type=Rock, count=3) and self.has(
            resource_type=Wheat, count=2
        )

    def can_buy_development_card(self):
        return (
            self.has(resource_type=Rock, count=1)
            and self.has(resource_type=Sheep, count=1)
            and self.has(resource_type=Wheat, count=1)
        )
