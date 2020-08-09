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

    def has(self, resource_type: ResourceType, count: int) -> bool:
        return self.hand[resource_type] >= count

    def add(self, resource_type: ResourceType, count: int) -> None:
        if not count > 0:
            raise RuntimeError("Cannot add 0 or less cards to the hand.")

        self.hand[resource_type] += count

    def remove(self, resource_type: ResourceType, count: int) -> int:
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
