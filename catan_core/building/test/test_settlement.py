from catan_core.building.settlement import Settlement


class TestSettlement:
    def test_init_player(self):
        settlement = Settlement(player="p1")
        assert settlement.player == "p1"

    def test_init_payout_count(self):
        settlement = Settlement(player="p1")
        assert settlement.payout == 1

    def test_init_victory_points(self):
        settlement = Settlement(player="p1")
        assert settlement.victory_points == 1

    def test_eq_returns_true(self):
        assert Settlement(player="p1") == Settlement(player="p1")

    def test_eq_retruns_false(self):
        assert Settlement(player="p1") != Settlement(player="p2")
