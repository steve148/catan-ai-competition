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

    def test_eq_returns_false_if_name_different(self):
        assert Action(name="a") != Action(name="b")

    def test_eq_returns_false_if_kwargs_different(self):
        assert Action(name="a", kwargs={"a": 1}) != Action(name="a", kwargs={"a": 2})

    def test_eq_returns_true_if_name_is_equal(self):
        assert Action(name="x") == Action(name="x")

    def test_eq_returns_true_if_name_and_kwargs_are_equal(self):
        assert Action(name="x", kwargs={"a": 1}) == Action(name="x", kwargs={"a": 1})
