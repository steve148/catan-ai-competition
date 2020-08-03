from catan_core.development_card.deck import DevelopmentCardDeck
from catan_core.development_card.knight_card import KnightDevelopmentCard
from catan_core.development_card.monopoly_card import MonopolyDevelopmentCard
from catan_core.development_card.road_building_card import RoadBuildingDevelopmentCard
from catan_core.development_card.victory_point_card import VictoryPointDevelopmentCard
from catan_core.development_card.year_of_plenty_card import YearOfPlentyDevelopmentCard


class TestDevelopmentCardDeck:
    def test_init_list_of_development_cards(self):
        deck = DevelopmentCardDeck()
        assert hasattr(deck, "cards")

    def test_init_fourteen_knight_cards(self):
        deck = DevelopmentCardDeck()
        knight_cards = [
            card for card in deck.cards if isinstance(card, KnightDevelopmentCard)
        ]
        assert len(knight_cards) == 14

    def test_init_two_monopoloy_cards(self):
        deck = DevelopmentCardDeck()
        monopoly_cards = [
            card for card in deck.cards if isinstance(card, MonopolyDevelopmentCard)
        ]
        assert len(monopoly_cards) == 2

    def test_init_two_year_of_plenty_cards(self):
        deck = DevelopmentCardDeck()
        year_of_plenty_cards = [
            card for card in deck.cards if isinstance(card, YearOfPlentyDevelopmentCard)
        ]
        assert len(year_of_plenty_cards) == 2

    def test_init_two_road_building_cards(self):
        deck = DevelopmentCardDeck()
        road_building_cards = [
            card for card in deck.cards if isinstance(card, RoadBuildingDevelopmentCard)
        ]
        assert len(road_building_cards) == 2

    def test_init_five_victory_point_cards(self):
        deck = DevelopmentCardDeck()
        road_building_cards = [
            card for card in deck.cards if isinstance(card, VictoryPointDevelopmentCard)
        ]
        assert len(road_building_cards) == 5

    def test_draw_card_from_deck(self):
        deck = DevelopmentCardDeck()
        previous_count = len(deck.cards)
        deck.draw()
        new_count = len(deck.cards)
        assert previous_count == new_count + 1
