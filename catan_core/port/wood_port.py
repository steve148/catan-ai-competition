from catan_core.port.port import Port
from catan_core.resource_type.wood import Wood


class WoodPort(Port):
    def __init__(self):
        self.resource_types = [Wood]
        self.ratio = 2
