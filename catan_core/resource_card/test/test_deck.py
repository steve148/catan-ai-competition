import pytest

from catan_core.resource_card.deck import ResourceCardDeck


class TestResourceCardDeck:
    def test_init_dict_of_resource_cards(self):
        deck = ResourceCardDeck()
        assert hasattr(deck, "cards")
        assert isinstance(deck.cards, dict)

    def test_init_nineteen_wheat(self):
        deck = ResourceCardDeck()
        assert deck.cards.get("wheat") == 19

    def test_init_nineteen_wood(self):
        deck = ResourceCardDeck()
        assert deck.cards.get("wood") == 19

    def test_init_nineteen_sheep(self):
        deck = ResourceCardDeck()
        assert deck.cards.get("sheep") == 19

    def test_init_nineteen_clay(self):
        deck = ResourceCardDeck()
        assert deck.cards.get("clay") == 19

    def test_init_nineteen_rock(self):
        deck = ResourceCardDeck()
        assert deck.cards.get("rock") == 19

    def test_draw_invalid_resource_type(self):
        deck = ResourceCardDeck()
        with pytest.raises(
            ValueError, match=r"Resource must be one of the following .*"
        ):
            deck.draw("not a resource", 1)

    def test_draw_zero_or_less(self):
        deck = ResourceCardDeck()
        with pytest.raises(ValueError, match=r"Amount must be greater than zero"):
            deck.draw("rock", 0)

    def test_amount_fully_available(self):
        deck = ResourceCardDeck()
        cards = deck.draw("rock", 5)
        assert cards == 5
        assert deck.cards["rock"] == 14

    def test_amount_not_available(self):
        deck = ResourceCardDeck()
        cards = deck.draw("rock", 20)
        assert cards == 19
        assert deck.cards["rock"] == 0
