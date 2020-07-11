from catan_core.building.settlement import Settlement
from catan_core.board import Board


class TestBoard:
    """Tests for the Board class."""

    def test_nineteen_hexes(self):
        assert len(Board().hexes) == 19

    def test_fifty_four_vertices(self):
        assert len(Board().vertices) == 54

    def test_seventy_two_edges(self):
        assert len(Board().edges) == 72

    def test_victory_points_for_player_no_buildings(self):
        assert Board().victory_points_for_player(player="p1") == 0

    def test_victory_points_for_player_with_buildings(self):
        building = Settlement(player="p1")
        board = Board()
        board.vertices[0].building = building

        assert board.victory_points_for_player("p1") == 1
