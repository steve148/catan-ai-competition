from catan_core.port.port import Port
from catan_core.resource_type.clay import Clay
from catan_core.resource_type.rock import Rock
from catan_core.resource_type.sheep import Sheep
from catan_core.resource_type.wheat import Wheat
from catan_core.resource_type.wood import Wood


class AnyResourcePort(Port):
    def __init__(self):
        self.resource_types = [Clay, Rock, Sheep, Wheat, Wood]
        self.ratio = 3
