"""Step 2: Magic Methods

Tests for dunder methods that make Config behave like a native Python object.
"""

from configkit.config import Config


class TestRepr:
    def test_repr_shows_key_count(self):
        """repr should show class name and number of top-level keys."""
        config = Config({"a": 1, "b": 2, "c": 3})
        assert repr(config) == "Config(keys=3)"

    def test_repr_empty(self):
        config = Config({})
        assert repr(config) == "Config(keys=0)"


class TestGetItem:
    def test_bracket_access(self):
        """config['key'] should work like config.get('key')."""
        config = Config({"database": {"host": "localhost"}})
        assert config["database"] == {"host": "localhost"}

    def test_bracket_dot_notation(self):
        """config['a.b'] should support dot-notation."""
        config = Config({"database": {"host": "localhost"}})
        assert config["database.host"] == "localhost"

    def test_bracket_missing_raises_keyerror(self):
        """config['missing'] should raise KeyError."""
        config = Config({"a": 1})
        try:
            _ = config["missing"]
            assert False, "Should have raised KeyError"
        except KeyError:
            pass


class TestContains:
    def test_contains_top_level(self):
        """'key' in config should return True for existing keys."""
        config = Config({"a": 1, "b": 2})
        assert "a" in config
        assert "c" not in config

    def test_contains_dot_notation(self):
        """'a.b' in config should check nested keys."""
        config = Config({"database": {"host": "localhost"}})
        assert "database.host" in config
        assert "database.port" not in config


class TestLen:
    def test_len_top_level_keys(self):
        """len(config) should return the number of top-level keys."""
        config = Config({"a": 1, "b": 2, "c": 3})
        assert len(config) == 3

    def test_len_empty(self):
        config = Config({})
        assert len(config) == 0


class TestIter:
    def test_iter_top_level_keys(self):
        """Iterating over config should yield top-level keys."""
        config = Config({"a": 1, "b": 2})
        keys = list(config)
        assert sorted(keys) == ["a", "b"]


class TestEq:
    def test_equal_configs(self):
        """Two configs with the same data should be equal."""
        config1 = Config({"a": 1, "b": 2})
        config2 = Config({"a": 1, "b": 2})
        assert config1 == config2

    def test_unequal_configs(self):
        """Two configs with different data should not be equal."""
        config1 = Config({"a": 1})
        config2 = Config({"a": 2})
        assert config1 != config2
