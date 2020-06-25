from catan_core.hex import Hex


class TestHex:
    def test_init(self):
        hex = Hex("rock", 5)
        assert hex.resource_type == "rock"
        assert hex.number == 5
