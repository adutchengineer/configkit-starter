import pytest

from configkit.config import Config


class TestConfigCreation:
    def test_config_creation(self):
        """Config should accept a dictionary and store its values.

        Example:
            config = Config({"database": {"host": "localhost", "port": 5432}})
            assert config.data == {"database": {"host": "localhost", "port": 5432}}
        """
        pytest.skip("Implement in Lesson 1")

    def test_config_empty(self):
        """Config created with no arguments should have empty data."""
        pytest.skip("Implement in Lesson 1")


class TestConfigAccess:
    def test_config_get_value(self):
        """Config should support getting values by key.

        Example:
            config = Config({"database": {"host": "localhost"}})
            assert config.get("database") == {"host": "localhost"}
        """
        pytest.skip("Implement in Lesson 1")

    def test_config_get_nested_value(self):
        """Config should support dot-notation for nested access.

        Example:
            config = Config({"database": {"host": "localhost"}})
            assert config.get("database.host") == "localhost"
        """
        pytest.skip("Implement in Lesson 2")

    def test_config_get_missing_key(self):
        """Config.get should return a default value for missing keys.

        Example:
            config = Config({"database": {"host": "localhost"}})
            assert config.get("missing", default="fallback") == "fallback"
        """
        pytest.skip("Implement in Lesson 2")


class TestConfigRepr:
    def test_config_repr(self):
        """Config repr should show the class name and number of top-level keys.

        Example:
            config = Config({"a": 1, "b": 2})
            assert repr(config) == "Config(keys=2)"
        """
        pytest.skip("Implement in Lesson 1")
