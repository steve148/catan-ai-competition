from catan_core.player.player import Player
from catan_core.road import Road


class TestRoad:
    def test_init_player(self):
        player = Player()
        road = Road(player=player)
        assert road.player == player

    def test_eq_returns_false(self):
        player = Player()
        other_player = Player()
        assert Road(player=player) != Road(player=other_player)

    def test_eq_returns_true(self):
        player = Player()
        assert Road(player=player) == Road(player=player)
