from catan_core.board import Board


class TestBoard:
    """Tests for the Board class."""

    def test_nineteen_hexes(self):
        assert len(Board().hexes) == 19
