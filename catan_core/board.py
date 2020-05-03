class Vertex:
    def __init__(self, position):
        self.position = position


class Hex:
    def __init__(self, position):
        self.position = position
        self.vertices = [Vertex(i) for i in range(6)]


class Board:
    """
    Class which stores the state of the board for a game.
    """

    def __init__(self):
        self.hexes = [Hex(i) for i in range(19)]
