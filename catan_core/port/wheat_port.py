from catan_core.port.port import Port
from catan_core.resource_type.wheat import Wheat


class WheatPort(Port):
    def __init__(self):
        self.resource_types = [Wheat]
        self.ratio = 2
