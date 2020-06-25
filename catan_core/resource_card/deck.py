from catan_core.resource_type.clay import Clay
from catan_core.resource_type.rock import Rock
from catan_core.resource_type.sheep import Sheep
from catan_core.resource_type.wheat import Wheat
from catan_core.resource_type.wood import Wood

resource_types = [Clay, Rock, Sheep, Wheat, Wood]


class ResourceCardDeck:
    def __init__(self):
        self.cards = {}
        for resource in resource_types:
            self.cards[resource] = 19

    def draw(self, resource: str, amount: int) -> int:
        if resource not in resource_types:
            raise ValueError(f"Resource must be one of the following {resource_types}")

        if amount < 1:
            raise ValueError("Amount must be greater than zero")

        if self.cards[resource] < amount:
            number_cards_to_draw = self.cards[resource]
        else:
            number_cards_to_draw = amount

        self.cards[resource] -= amount
        if self.cards[resource] < 0:
            self.cards[resource] = 0

        return number_cards_to_draw
