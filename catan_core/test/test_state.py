from catan_core.state import State
from catan_core.development_card.deck import DevelopmentCardDeck


class TestState:
    """Tests for State class."""

    def test_init_resource_cards(self):
        """Check that initial state of game includes all resource cards."""
        state = State()
        assert state.resource_cards == [
            {"type": "wheat", "available": 19},
            {"type": "wood", "available": 19},
            {"type": "sheep", "available": 19},
            {"type": "clay", "available": 19},
            {"type": "rock", "available": 19},
        ]

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
