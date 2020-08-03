from catan_core.port.wheat_port import WheatPort
from catan_core.resource_type.wheat import Wheat


class TestWheatPort:
    def test_resource_types(self):
        assert Wheat in WheatPort().resource_types

    def test_ratio(self):
        assert WheatPort().ratio == 2
