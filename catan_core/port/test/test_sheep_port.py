from catan_core.resource_type.sheep import Sheep
from catan_core.port.sheep_port import SheepPort


class TestSheepPort:
    def test_resource_types(self):
        assert Sheep in SheepPort().resource_types

    def test_ratio(self):
        assert SheepPort().ratio == 2
