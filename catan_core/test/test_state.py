from catan_core.board import Board
from catan_core.building.city import City
from catan_core.building.settlement import Settlement
from catan_core.development_card.deck import DevelopmentCardDeck
from catan_core.resource_card.deck import ResourceCardDeck
from catan_core.state import State


class TestState:
    """Tests for State class."""

    def test_init_resource_cards(self):
        """Check that initial state of game includes all resource cards."""
        state = State(players=["p1"])
        assert isinstance(state.resource_card_deck, ResourceCardDeck)

    def test_init_deck_of_development_cards(self):
        state = State(players=["p1"])
        assert isinstance(state.development_card_deck, DevelopmentCardDeck)

    def test_init_board(self):
        state = State(players=["p1"])
        assert isinstance(state.board, Board)

    def test_init_player_pieces(self):
        """Check that initial state of game includes pieces for each player."""
        state = State(players=["p1"])
        assert state.player_pieces == {
            "p1": {"cities": 4, "roads": 15, "settlements": 5}
        }

    def test_init_bonus_victory_points_tracker(self):
        state = State(players=["p1"])
        assert state.bonus_victory_points == {
            "p1": {
                "victory_point_development_cards": 0,
                "longest_road": False,
                "largest_army": False,
            }
        }

    def test_init_player_order_includes_all_players(self):
        players = ["p1", "p2", "p3", "p4"]
        state = State(players=players)
        for player in players:
            assert player in state.players

    def test_init_current_player_turn(self):
        players = ["p1", "p2", "p3", "p4"]
        state = State(players=players)
        assert state.current_player_turn == state.players[0]

    def test_init_dice_rolled(seslf):
        state = State(players=["p1"])
        assert not state.dice_rolled

    def test_is_game_over_no_player_won(self):
        state = State(players=["p1", "p2"])
        assert not state.is_game_over()

    def test_is_game_over_player_has_won(self):
        state = State(players=["p1", "p2"])

        state.board.vertices[0].building = City(player="p1")
        state.board.vertices[1].building = Settlement(player="p1")
        state.bonus_victory_points["p1"]["victory_point_development_cards"] = 3
        state.bonus_victory_points["p1"]["longest_road"] = True
        state.bonus_victory_points["p1"]["largest_army"] = True

        assert state.is_game_over() == "p1"

    def test_player_actions_roll_dice_roll_if_not_done(self):
        state = State(players=["p1"])
        actions = state.player_actions(player=state.current_player_turn)
        assert {"name": "roll_dice"} in actions

    def test_player_actions_no_roll_dice_if_already_done(self):
        state = State(players=["p1"])
        state.dice_rolled = True
        actions = state.player_actions(player=state.current_player_turn)
        assert {"name": "roll_dice"} not in actions

    def test_player_actions_end_turn(self):
        state = State(players=["p1"])
        state.dice_rolled = True
        actions = state.player_actions(player=state.current_player_turn)
        assert {"name": "end_turn"} in actions
