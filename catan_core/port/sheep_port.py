from catan_core.port.port import Port
from catan_core.resource_type.sheep import Sheep


class SheepPort(Port):
    def __init__(self):
        self.resource_types = [Sheep]
        self.ratio = 2
