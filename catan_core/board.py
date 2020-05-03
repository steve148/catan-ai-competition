class Hex:
    def __init__(self):
        pass


class Board:
    """
    Class which stores the state of the board for a game.
    """

    def __init__(self):
        self.hexes = [Hex() for i in range(19)]
