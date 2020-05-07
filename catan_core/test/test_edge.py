from catan_core.edge import Edge
from catan_core.vertex import Vertex


class TestEdge:
    def test_init_no_vertices(self):
        assert Edge().vertices == []

    def test_set_vertices(self):
        edge = Edge()
        vertex = Vertex()

        edge.vertices = [vertex]

        assert edge.vertices == [vertex]
