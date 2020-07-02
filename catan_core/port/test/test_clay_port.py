from catan_core.port.clay_port import ClayPort
from catan_core.resource_type.clay import Clay


class TestClayPort:
    def test_resource_types(self):
        assert Clay in ClayPort().resource_types

    def test_ratio(self):
        assert ClayPort().ratio == 2
