from catan_core.development_card.base_card import BaseDevelopmentCard
from catan_core.development_card.road_building_card import RoadBuildingDevelopmentCard


class TestRoadBuildingDevelopmentCard:
    def test_sub_class_base_development_card(self):
        assert issubclass(RoadBuildingDevelopmentCard, BaseDevelopmentCard)
