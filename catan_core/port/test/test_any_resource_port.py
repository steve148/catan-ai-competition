from catan_core.port.any_resource_port import AnyResourcePort
from catan_core.resource_type.clay import Clay
from catan_core.resource_type.rock import Rock
from catan_core.resource_type.sheep import Sheep
from catan_core.resource_type.wheat import Wheat
from catan_core.resource_type.wood import Wood


class TestAnyResourcePort:
    def test_resource_types(self):
        port = AnyResourcePort()
        assert Rock in port.resource_types
        assert Clay in port.resource_types
        assert Sheep in port.resource_types
        assert Wheat in port.resource_types
        assert Wood in port.resource_types

    def test_ratio(self):
        assert AnyResourcePort().ratio == 3
