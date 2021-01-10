from catan_core.player.player import Player
from catan_core.road import Road


class TestRoad:
    def test_init_player(self):
        player = Player()
        road = Road(player=player)
        assert road.player == player
