from catan_core.action import Action
from catan_core.player.human_player import HumanPlayer


class TestHumanPlayer:
    def test_init(self):
        player = HumanPlayer(name="lenny")
        assert player.name == "lenny"

    def test_choose_action_prints_actions(self, mocker):
        print_mock = mocker.patch("builtins.print")
        mocker.patch("builtins.input", return_value="0")

        player = HumanPlayer(name="")
        actions = [Action(name="test_action")]

        player.choose_action(actions=actions)
        print_mock.assert_called_once_with(actions)

    def test_choose_action_based_on_input(self, mocker):
        mocker.patch("builtins.print")
        mocker.patch("builtins.input", return_value="0")

        player = HumanPlayer(name="")
        actions = [Action(name="test_action"), Action(name="another_action")]

        chosen = player.choose_action(actions=actions)
        assert chosen == actions[0]
