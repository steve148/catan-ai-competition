class Action:
    def __init__(self, name: str, kwargs: dict = None) -> None:
        self.name = name
        self.kwargs = kwargs

    def __eq__(self, o: object) -> bool:
        return self.name == o.name and self.kwargs == o.kwargs
