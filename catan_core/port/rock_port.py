from catan_core.port.port import Port
from catan_core.resource_type.rock import Rock


class RockPort(Port):
    def __init__(self):
        self.resource_types = [Rock]
        self.ratio = 2
