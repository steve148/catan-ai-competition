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

    def test_can_place_returns_false_if_road_already_exists(self):
        edge = Edge()
        player = Player()
        edge.road = Road(player=player)
        assert not edge.can_place_road(player=player)

    def test_can_place_road_returns_true(self):
        edge = Edge()
        player = Player()
        assert edge.can_place_road(player=player)
