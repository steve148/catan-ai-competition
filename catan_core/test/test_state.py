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
        state = State()
        assert isinstance(state.resource_card_deck, ResourceCardDeck)

    def test_init_player_pieces(self):
        """Check that initial state of game includes pieces for each player."""
        state = State(players=["p1", "p2"])
        assert state.player_pieces == [
            {"cities": 4, "player": "p1", "roads": 15, "settlements": 5},
            {"cities": 4, "player": "p2", "roads": 15, "settlements": 5},
        ]

    def test_init_deck_of_development_cards(self):
        state = State()
        assert isinstance(state.development_card_deck, DevelopmentCardDeck)

    def test_init_bonus_victory_points_tracker(self):
        state = State(players=["p1"])
        assert state.bonus_victory_points == {
            "p1": {
                "victory_point_development_cards": 0,
                "longest_road": False,
                "largest_army": False,
            }
        }

    def test_init_board(self):
        state = State()
        assert isinstance(state.board, Board)

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
