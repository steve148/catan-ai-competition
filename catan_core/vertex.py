from typing import List

from catan_core.edge import Edge
from catan_core.port.port import Port


class Vertex:
    def __init__(self, port: Port = None):
        self.edges: List[Edge] = []
        self.port = port
