from catan_core.hex import Hex


class TestHex:
    def test_init_resource_type(self):
        hex = Hex("rock")
        assert hex.resource_type == "rock"
