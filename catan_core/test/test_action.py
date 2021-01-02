from catan_core.action import Action


class TestAction:
    def test_init(self):
        action = Action(name="build_something", kwargs={"key": "value"})
        assert action.name == "build_something"
        assert action.kwargs == {"key": "value"}
