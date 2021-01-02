import pytest

from catan_core.building.building import Building
from catan_core.building.settlement import Settlement
from catan_core.edge import Edge
from catan_core.player.player import Player
from catan_core.port.rock_port import RockPort
from catan_core.road import Road
from catan_core.vertex import Vertex


class TestVertex:
    def test_init(self):
        port = RockPort()
        vertex = Vertex(id=0, port=port)

        assert vertex.id == 0
        assert vertex.edges == []
        assert vertex.hexes == []
        assert vertex.port == port
        assert not vertex.building

    def test_repr(self):
        assert Vertex(id=0).__repr__() == "vertex-0"

    def test_assign_building_raises_error_if_already_assigned(self):
        vertex = Vertex(id=0)
        vertex.building = Building()
        with pytest.raises(
            RuntimeError, match=r"A building already exists at this vertex"
        ):
            vertex.assign_building(building=Building())

    def test_assign_building_successfully(self):
        vertex = Vertex(id=0)
        building = Building()
        vertex.assign_building(building=building)
        assert vertex.building == building

    def test_can_place_building_returns_false_if_building_exists(self):
        player = Player()
        vertex = Vertex(id=0)
        edge = Edge(id=0)

        edge.vertices = [vertex]
        edge.road = Road(player)
        vertex.edges = [edge]
        vertex.assign_building(building=Settlement(player=player))

        assert not vertex.can_place_building(player=player)

    def test_can_place_building_returns_false_if_no_roads_exist(self):
        player = Player()
        different_player = Player()
        vertex = Vertex(id=0)
        edge_no_road = Edge(id=0)
        edge_road_different_player = Edge(id=1)

        vertex.edges = [edge_no_road, edge_road_different_player]
        edge_no_road.vertices = [vertex]
        edge_road_different_player.vertices = [vertex]
        edge_road_different_player.road = Road(player=different_player)

        assert not vertex.can_place_building(player=player)

    def test_can_place_building_Returns_false_if_building_is_nearby(self):
        player = Player()
        vertex = Vertex(id=0)
        neighbour_vertex = Vertex(id=1)
        edge = Edge(id=0)

        vertex.edges = [edge]
        neighbour_vertex.edges = [edge]
        neighbour_vertex.building = Settlement(player=player)
        edge.vertices = [vertex, neighbour_vertex]
        edge.road = Road(player=player)

        assert not vertex.can_place_building(player=player)

    def test_can_place_building_returns_true(self):
        player = Player()
        vertex = Vertex(id=0)
        edge = Edge(id=0)
        neighbour_vertex = Vertex(id=1)

        edge.road = Road(player)
        vertex.edges = [edge]
        neighbour_vertex.edges = [edge]
        edge.vertices = [vertex, neighbour_vertex]

        assert vertex.can_place_building(player=player)
