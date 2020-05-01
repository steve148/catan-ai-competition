from catan_core.state import State


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

    def test_init_development_cards(self):
        """Check that initial state of game includes all development cards."""
        state = State()
        cards = state.development_cards
        assert len([card for card in cards if card["type"] == "knight"]) == 14
        assert len([card for card in cards if card["type"] == "monopoly"]) == 2
        assert len([card for card in cards if card["type"] == "road_building"]) == 2
        assert len([card for card in cards if card["type"] == "year_of_plenty"]) == 2
        assert len([card for card in cards if card["type"] == "victory"]) == 5

    def test_init_development_cards_shuffled(self):
        """Check that initial state of game includes shuffled set of development cards."""
        state1 = State()
        state2 = State()

        assert state1.development_cards != state2.development_cards
