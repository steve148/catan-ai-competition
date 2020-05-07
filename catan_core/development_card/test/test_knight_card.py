from catan_core.development_card.base_card import BaseDevelopmentCard
from catan_core.development_card.knight_card import KnightDevelopmentCard


class TestKnightDevelopmentCard:
    def test_sub_class_base_development_card(self):
        assert issubclass(KnightDevelopmentCard, BaseDevelopmentCard)
