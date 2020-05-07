class Vertex:
    def __init__(self):
        self._edges = []

    @property
    def edges(self):
        return self._edges

    def add_edge(self, edge):
        self._edges.append(edge)
