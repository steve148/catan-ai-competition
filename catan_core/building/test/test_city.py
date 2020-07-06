from catan_core.building.city import City


class TestCity:
    def test_init_player(self):
        city = City(player="p1")
        assert city.player == "p1"

    def test_init_payout_count(self):
        city = City(player="p1")
        assert city.payout == 2
