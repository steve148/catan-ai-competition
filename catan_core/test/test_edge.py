import pytest

from catan_core.edge import Edge
from catan_core.player.player import Player
from catan_core.road import Road
from catan_core.vertex import Vertex


class TestEdge:
    def test_init_no_vertices(self):
        assert Edge().vertices == []

    def test_set_vertices(self):
        edge = Edge()
        vertex = Vertex()

        edge.vertices = [vertex]

        assert edge.vertices == [vertex]

    def test_palce_road_already_exists(self):
        edge = Edge()
        player = Player()
        edge.road = Road(player=player)

        with pytest.raises(RuntimeError, match="Edge already has a road placed on it."):
            edge.place_road(player=player)

    def test_place_road_no_road_yet(self):
        edge = Edge()
        player = Player()

        assert not edge.road

        edge.place_road(player=player)

        assert isinstance(edge.road, Road)
