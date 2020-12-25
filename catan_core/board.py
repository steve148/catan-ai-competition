import random

from catan_core.edge import Edge
from catan_core.hex import Hex
from catan_core.player.player import Player
from catan_core.resource_type.clay import Clay
from catan_core.resource_type.rock import Rock
from catan_core.resource_type.sheep import Sheep
from catan_core.resource_type.wheat import Wheat
from catan_core.resource_type.wood import Wood
from catan_core.vertex import Vertex


class Board:
    """
    Class which stores the state of the board for a game.
    """

    def __init__(self):
        # Randomly select resource type and number for each hex.
        self.hexes = self.setup_hexes()

        self.vertices = [Vertex() for i in range(54)]

        self.edges = [Edge() for i in range(72)]

        for hex_index, vertex_indices in enumerate(hex_to_vertex):
            hex = self.hexes[hex_index]

            for vertex_index in vertex_indices:

                vertex = self.vertices[vertex_index]

                hex.vertices.append(vertex)

        for edge_index, vertex_indices in enumerate(edge_to_vertices):
            edge = self.edges[edge_index]

            for vertex_index in vertex_indices:
                vertex = self.vertices[vertex_index]

                vertex.edges.append(edge)

                edge.vertices.append(vertex)

    def setup_hexes(self):
        # Define how many of each resource should be on the board.
        resource_types = (3 * [Rock, Clay]) + (4 * [Wood, Wheat, Sheep])
        random.shuffle(resource_types)

        # There should be two of each hex number on the board.
        # 2 and 12 are the exception with only 1 instance of each.
        numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        random.shuffle(numbers)

        # Combine the two lists and add the hex values for the dessert tile.
        hex_values = [list(a) for a in zip(resource_types, numbers)] + [(None, 7)]
        random.shuffle(hex_values)

        # Use the shuffled hex values to create each hex instance on the board.
        hexes = []
        for resource_type, number in hex_values:
            hexes.append(Hex(resource_type, number))

        return hexes

    def victory_points_for_player(self, player: Player) -> int:
        return sum(
            [
                vertex.building.victory_points
                for vertex in self.vertices
                if vertex.building and vertex.building.player == player
            ]
        )


edge_to_vertices = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (0, 8),
    (2, 10),
    (4, 12),
    (6, 14),
    (7, 8),
    (8, 9),
    (9, 10),
    (10, 11),
    (11, 12),
    (12, 13),
    (13, 14),
    (14, 15),
    (7, 17),
    (9, 19),
    (11, 21),
    (13, 23),
    (15, 25),
    (16, 17),
    (17, 18),
    (18, 19),
    (19, 20),
    (20, 21),
    (21, 22),
    (22, 23),
    (23, 24),
    (24, 25),
    (25, 26),
    (16, 27),
    (18, 29),
    (20, 31),
    (22, 33),
    (24, 35),
    (26, 37),
    (27, 28),
    (28, 29),
    (29, 30),
    (30, 31),
    (31, 32),
    (32, 33),
    (33, 34),
    (34, 35),
    (35, 36),
    (36, 37),
    (28, 38),
    (30, 40),
    (32, 42),
    (34, 44),
    (36, 46),
    (38, 39),
    (39, 40),
    (40, 41),
    (41, 42),
    (42, 43),
    (43, 44),
    (44, 45),
    (45, 46),
    (39, 47),
    (41, 49),
    (43, 51),
    (45, 53),
    (47, 48),
    (48, 49),
    (49, 50),
    (50, 51),
    (51, 52),
    (52, 53),
]


hex_to_vertex = [
    (0, 1, 2, 8, 9, 10),
    (2, 3, 4, 10, 11, 12),
    (4, 5, 6, 12, 13, 14),
    (7, 8, 9, 17, 18, 19),
    (9, 10, 11, 19, 20, 21),
    (11, 12, 13, 21, 22, 23),
    (13, 14, 15, 23, 24, 25),
    (16, 17, 18, 27, 28, 29),
    (18, 19, 20, 29, 30, 31),
    (20, 21, 22, 31, 32, 33),
    (22, 23, 24, 33, 34, 35),
    (24, 25, 26, 35, 36, 37),
    (28, 29, 30, 38, 39, 40),
    (30, 31, 32, 40, 41, 42),
    (32, 33, 34, 42, 43, 44),
    (34, 35, 36, 44, 45, 46),
    (39, 40, 41, 47, 48, 49),
    (41, 42, 43, 49, 50, 51),
    (43, 44, 45, 51, 52, 53),
]
