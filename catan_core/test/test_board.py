from catan_core.board import Board, Hex, Vertex


class TestHex:
    """Tests for the Hex class."""

    def test_six_vertices(self):
        assert len(Hex(0).vertices) == 6

    def test_position_attr(self):
        assert Hex(0).position == 0


class TestBoard:
    """Tests for the Board class."""

    def test_nineteen_hexes(self):
        assert len(Board().hexes) == 19

    def test_position_attr(self):
        assert Vertex(0).position == 0
