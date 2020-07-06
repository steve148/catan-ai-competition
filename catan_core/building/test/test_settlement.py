from catan_core.building.settlement import Settlement


class TestSettlement:
    def test_init_player(self):
        settlement = Settlement(player="p1")
        assert settlement.player == "p1"

    def test_init_payout_count(self):
        settlement = Settlement(player="p1")
        assert settlement.payout == 1
