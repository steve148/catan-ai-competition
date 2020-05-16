from catan_core.development_card.knight_card import KnightDevelopmentCard
from catan_core.development_card.monopoly_card import MonopolyDevelopmentCard
from catan_core.development_card.road_building_card import RoadBuildingDevelopmentCard
from catan_core.development_card.victory_point_card import VictoryPointDevelopmentCard
from catan_core.development_card.year_of_plenty_card import YearOfPlentyDevelopmentCard


class DevelopmentCardDeck:
    def __init__(self):
        self.cards = (
            [KnightDevelopmentCard() for i in range(14)]
            + [MonopolyDevelopmentCard() for i in range(2)]
            + [RoadBuildingDevelopmentCard() for i in range(2)]
            + [YearOfPlentyDevelopmentCard() for i in range(2)]
            + [VictoryPointDevelopmentCard() for i in range(5)]
        )
