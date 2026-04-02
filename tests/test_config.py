"""Step 1: Config Class

Tests for the core Config class — constructor, get/set with dot-notation,
and required key validation.
"""

import pytest

from configkit.config import Config


class TestConfigCreation:
    def test_create_with_dict(self):
        """Config should store the provided dictionary."""
        data = {"database": {"host": "localhost", "port": 5432}}
        config = Config(data)
        assert config._data == data

    def test_create_empty(self):
        """Config with no arguments should have empty data."""
        config = Config({})
        assert config._data == {}


class TestConfigGet:
    def test_get_top_level_key(self):
        """get('key') should return the value for a top-level key."""
        config = Config({"database": {"host": "localhost"}})
        assert config.get("database") == {"host": "localhost"}

    def test_get_dot_notation(self):
        """get('a.b.c') should walk nested dicts."""
        config = Config({"database": {"host": "localhost", "port": 5432}})
        assert config.get("database.host") == "localhost"
        assert config.get("database.port") == 5432

    def test_get_missing_returns_default(self):
        """get() should return default when key is missing."""
        config = Config({"a": 1})
        assert config.get("b") is None
        assert config.get("b", "fallback") == "fallback"

    def test_get_missing_nested_returns_default(self):
        """get('a.b.c') should return default when intermediate key is missing."""
        config = Config({"a": 1})
        assert config.get("a.b.c", "nope") == "nope"


class TestConfigSet:
    def test_set_top_level(self):
        """set('key', value) should set a top-level key."""
        config = Config({})
        config.set("host", "localhost")
        assert config.get("host") == "localhost"

    def test_set_dot_notation_creates_nested(self):
        """set('a.b.c', value) should create intermediate dicts."""
        config = Config({})
        config.set("database.host", "localhost")
        assert config._data == {"database": {"host": "localhost"}}

    def test_set_overwrites_existing(self):
        """set() should overwrite an existing value."""
        config = Config({"database": {"host": "old"}})
        config.set("database.host", "new")
        assert config.get("database.host") == "new"


class TestConfigValidation:
    def test_required_keys_present(self):
        """No error when all required keys are present."""
        config = Config({"database": {"host": "localhost"}, "debug": True})
        # Should not raise
        config = Config(
            {"database": {"host": "localhost"}, "debug": True},
            required_keys=["debug"],
        )

    def test_required_keys_missing_raises(self):
        """ValueError when a required key is missing."""
        with pytest.raises(ValueError):
            Config({"a": 1}, required_keys=["b"])

    def test_required_keys_dot_notation(self):
        """Required keys should support dot-notation paths."""
        with pytest.raises(ValueError):
            Config({"database": {}}, required_keys=["database.host"])
