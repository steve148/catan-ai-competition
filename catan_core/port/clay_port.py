from catan_core.port.port import Port
from catan_core.resource_type.clay import Clay


class ClayPort(Port):
    def __init__(self):
        self.resource_types = [Clay]
        self.ratio = 2
