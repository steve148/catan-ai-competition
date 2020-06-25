import pytest

from catan_core.resource_card.deck import ResourceCardDeck
from catan_core.resource_type.clay import Clay
from catan_core.resource_type.rock import Rock
from catan_core.resource_type.sheep import Sheep
from catan_core.resource_type.wheat import Wheat
from catan_core.resource_type.wood import Wood


class TestResourceCardDeck:
    def test_init_dict_of_resource_cards(self):
        deck = ResourceCardDeck()
        assert hasattr(deck, "cards")
        assert isinstance(deck.cards, dict)

    def test_init_nineteen_wheat(self):
        deck = ResourceCardDeck()
        assert deck.cards.get(Wheat) == 19

    def test_init_nineteen_wood(self):
        deck = ResourceCardDeck()
        assert deck.cards.get(Wood) == 19

    def test_init_nineteen_sheep(self):
        deck = ResourceCardDeck()
        assert deck.cards.get(Sheep) == 19

    def test_init_nineteen_clay(self):
        deck = ResourceCardDeck()
        assert deck.cards.get(Clay) == 19

    def test_init_nineteen_rock(self):
        deck = ResourceCardDeck()
        assert deck.cards.get(Rock) == 19

    def test_draw_invalid_resource_type(self):
        deck = ResourceCardDeck()
        with pytest.raises(
            ValueError, match=r"Resource must be one of the following .*"
        ):
            deck.draw("not a resource", 1)

    def test_draw_zero_or_less(self):
        deck = ResourceCardDeck()
        with pytest.raises(ValueError, match=r"Amount must be greater than zero"):
            deck.draw(Rock, 0)

    def test_amount_fully_available(self):
        deck = ResourceCardDeck()
        cards = deck.draw(Rock, 5)
        assert cards == 5
        assert deck.cards[Rock] == 14

    def test_amount_not_available(self):
        deck = ResourceCardDeck()
        cards = deck.draw(Rock, 20)
        assert cards == 19
        assert deck.cards[Rock] == 0
