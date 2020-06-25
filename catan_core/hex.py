from catan_core.resource_type.resource_type import ResourceType


class Hex:
    def __init__(self, resource_type: ResourceType, number: int):
        self.resource_type = resource_type
        self.number = number
