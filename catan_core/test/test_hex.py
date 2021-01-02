from catan_core.hex import Hex
from catan_core.resource_type.rock import Rock


class TestHex:
    def test_init(self):
        hex = Hex(id=0, resource_type=Rock, dice_number=5)
        assert hex.id == 0
        assert hex.resource_type == Rock
        assert hex.dice_number == 5
        assert hex.vertices == []
        assert not hex.robber

    def test_repr(self):
        assert Hex(id=0, resource_type=Rock, dice_number=5).__repr__() == "hex-0"

    def test_robber_exists_after_placing(self):
        hex = Hex(id=0, resource_type=Rock, dice_number=5)
        assert not hex.robber
        hex.place_robber()
        assert hex.robber

    def test_robber_gone_after_removing(self):
        hex = Hex(id=0, resource_type=Rock, dice_number=5)
        hex.place_robber()
        assert hex.robber
        hex.remove_robber()
        assert not hex.robber
