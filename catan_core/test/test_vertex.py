import pytest

from catan_core.building.building import Building
from catan_core.edge import Edge
from catan_core.port.rock_port import RockPort
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
