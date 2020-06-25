from catan_core.resource_type.rock import Rock
from catan_core.hex import Hex


class TestHex:
    def test_init(self):
        hex = Hex(Rock, 5)
        assert hex.resource_type == Rock
        assert hex.number == 5
