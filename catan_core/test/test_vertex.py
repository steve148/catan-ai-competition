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
