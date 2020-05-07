from catan_core.development_card.base_card import BaseDevelopmentCard
from catan_core.development_card.monopoly_card import MonopolyDevelopmentCard


class TestMonopolyDevelopmentCard:
    def test_sub_class_base_development_card(self):
        assert issubclass(MonopolyDevelopmentCard, BaseDevelopmentCard)
