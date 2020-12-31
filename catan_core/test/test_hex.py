from catan_core.hex import Hex
from catan_core.resource_type.rock import Rock


class TestHex:
    def test_init(self):
        hex = Hex(Rock, 5)
        assert hex.resource_type == Rock
        assert hex.number == 5
        assert hex.vertices == []
        assert not hex.robber
