from catan_core.board import Board


class TestBoard:
    """Tests for the Board class."""

    def test_nineteen_hexes(self):
        assert len(Board().hexes) == 19

    def test_fifty_four_vertices(self):
        assert len(Board().vertices) == 54

    def test_seventy_two_edges(self):
        assert len(Board().edges) == 72
