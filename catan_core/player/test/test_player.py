from catan_core.player.player import Player


class TestPlayer:
    def test_choose_action_exists(self):
        player = Player()
        assert hasattr(player, "choose_action")
        assert not player.choose_action(actions=[])
