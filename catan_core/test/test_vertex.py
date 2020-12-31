import pytest

from catan_core.building.building import Building
from catan_core.building.settlement import Settlement
from catan_core.edge import Edge
from catan_core.player.player import Player
from catan_core.port.rock_port import RockPort
from catan_core.road import Road
from catan_core.vertex import Vertex


class TestVertex:
    def test_init_no_edges(self):
        vertex = Vertex()

        assert vertex.edges == []

    def test_init_port(self):
        port = RockPort()
        vertex = Vertex(port=port)

        assert vertex.port == port

    def test_assign_building_raises_error_if_already_assigned(self):
        vertex = Vertex()
        vertex.building = Building()
        with pytest.raises(
            RuntimeError, match=r"A building already exists at this vertex"
        ):
            vertex.assign_building(building=Building())

    def test_assign_building_successfully(self):
        vertex = Vertex()
        building = Building()
        vertex.assign_building(building=building)
        assert vertex.building == building

    def test_can_place_building_returns_false_if_buidling_exists(self):
        player = Player()
        vertex = Vertex()

        vertex.building = Settlement(player=player)

        assert not vertex.can_place_building(player=player)

    def test_can_place_building_returns_false_if_no_roads_exist(self):
        player = Player()
        different_player = Player()
        vertex = Vertex()
        edge_no_road = Edge()
        edge_road_different_player = Edge()

        vertex.edges = [edge_no_road, edge_road_different_player]
        edge_no_road.vertices = [vertex]
        edge_road_different_player.vertices = [vertex]
        edge_road_different_player.road = Road(player=different_player)

        assert not vertex.can_place_building(player=player)

    def test_can_place_building_Returns_false_if_building_is_nearby(self):
        player = Player()
        vertex = Vertex()
        neighbour_vertex = Vertex()
        edge = Edge()

        vertex.edges = [edge]
        neighbour_vertex.edges = [edge]
        neighbour_vertex.building = Settlement(player=player)
        edge.vertices = [vertex, neighbour_vertex]
        edge.road = Road(player=player)

        assert not vertex.can_place_building(player=player)

    def test_can_place_building_returns_true(self):
        player = Player()
        vertex = Vertex()
        edge = Edge()
        neighbour_vertex = Vertex()

        edge.road = Road(player)
        vertex.edges = [edge]
        neighbour_vertex.edges = [edge]
        edge.vertices = [vertex, neighbour_vertex]

        assert vertex.can_place_building(player=player)
