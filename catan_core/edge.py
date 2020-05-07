class Edge:
    def __init__(self):
        self._vertices = []

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        self._vertices = vertices
