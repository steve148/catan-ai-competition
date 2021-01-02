from catan_core.action import Action


class TestAction:
    def test_init(self):
        action = Action(name="build_something")
        assert action.name == "build_something"
        assert not action.kwargs

    def test_init_with_kwargs(self):
        action = Action(name="build_something", kwargs={"key": "value"})
        assert action.name == "build_something"
        assert action.kwargs == {"key": "value"}
