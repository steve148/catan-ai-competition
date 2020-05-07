from catan_core.edge import Edge
from catan_core.vertex import Vertex


class TestVertex:
    def test_init_no_edges(self):
        vertex = Vertex()

        assert vertex.edges == []

    def test_add_edge(self):
        vertex = Vertex()
        edge = Edge()

        vertex.add_edge(edge)

        assert vertex.edges == [edge]
