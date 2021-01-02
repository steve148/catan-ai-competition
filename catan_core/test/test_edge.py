from catan_core.edge import Edge
from catan_core.player.player import Player
from catan_core.road import Road
from catan_core.vertex import Vertex


class TestEdge:
    def test_init_no_vertices(self):
        edge = Edge(id=0)
        assert edge.id == 0
        assert edge.vertices == []

    def test_repr(self):
        assert Edge(id=0).__repr__() == "edge-0"

    def test_set_vertices(self):
        edge = Edge(id=0)
        vertex = Vertex(id=0)

        edge.vertices = [vertex]

        assert edge.vertices == [vertex]

    def test_can_place_road_returns_false_if_road_already_exists(self):
        edge = Edge(id=0)
        player = Player()
        edge.road = Road(player=player)
        assert not edge.can_place_road(player=player)

    def test_can_place_road_returns_false_if_no_adjacent_roads_for_player(
        self,
    ):
        player1 = Player()
        player2 = Player()

        edge = Edge(id=0)
        edge_no_road = Edge(id=1)
        edge_with_road_player2 = Edge(id=2)
        edge_with_road_player2.road = Road(player=player2)

        v1 = Vertex(id=0)
        v2 = Vertex(id=1)

        # Connect vertex to edges
        edge.vertices = [v1, v2]
        edge_no_road.vertices = [v1]
        edge_with_road_player2.vertices = [v2]
        v1.edges = [edge, edge_no_road]
        v2.edges = [edge, edge_with_road_player2]

        assert not edge.can_place_road(player=player1)

    def test_can_place_road_returns_true_if_adjacent_road_for_player(self):
        player = Player()

        edge = Edge(id=0)
        edge_with_road = Edge(id=1)
        edge_with_road.road = Road(player=player)

        vertex = Vertex(id=0)

        # Connect vertex to edges
        edge.vertices = [vertex]
        edge_with_road.vertices = [vertex]
        vertex.edges = [edge, edge_with_road]

        assert edge.can_place_road(player=player)
