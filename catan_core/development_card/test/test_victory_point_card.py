from catan_core.development_card.base_card import BaseDevelopmentCard
from catan_core.development_card.year_of_plenty_card import YearOfPlentyDevelopmentCard


class TestYearOfPlentyDevelopmentCard:
    def test_sub_class_base_development_card(self):
        assert issubclass(YearOfPlentyDevelopmentCard, BaseDevelopmentCard)
