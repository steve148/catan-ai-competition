from catan_core.resource_type.rock import Rock
from catan_core.port.rock_port import RockPort


class TestRockPort:
    def test_resource_types(self):
        assert Rock in RockPort().resource_types

    def test_ratio(self):
        assert RockPort().ratio == 2
