from catan_core.board import Board, Hex


class TestHex:
    """Tests for the Hex class."""

    def test_six_vertices(self):
        assert len(Hex().vertices) == 6


class TestBoard:
    """Tests for the Board class."""

    def test_nineteen_hexes(self):
        assert len(Board().hexes) == 19
