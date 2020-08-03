from catan_core import actions
from catan_core.player.player import Player
from catan_core.state import State


class TestPlayerActions:
    def test_player_actions_no_actions(self):
        state = State(players=["p1"])
        player = Player()
        assert actions.player_actions(state=state, player=player) == []
