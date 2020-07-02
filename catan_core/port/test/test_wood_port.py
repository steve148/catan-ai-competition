from catan_core.port.wood_port import WoodPort
from catan_core.resource_type.wood import Wood


class TestWoodPort:
    def test_resource_type_is_wood(self):
        assert Wood in WoodPort().resource_types

    def test_ratio(self):
        assert WoodPort().ratio == 2
