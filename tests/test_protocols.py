"""Step 3: Protocols & Patterns

Tests for __call__, Loadable Protocol, and JSONLoader.
"""

import copy
import json

from configkit.config import Config


class TestCall:
    def test_call_returns_dict(self):
        """Calling config() should return a dictionary."""
        config = Config({"a": 1, "b": 2})
        result = config()
        assert isinstance(result, dict)

    def test_call_returns_deep_copy(self):
        """config() should return an independent copy, not a reference."""
        config = Config({"database": {"host": "localhost"}})
        result = config()
        result["database"]["host"] = "changed"
        assert config.get("database.host") == "localhost"


class TestLoadableProtocol:
    def test_json_loader_has_load(self):
        """JSONLoader should have a load() method."""
        from configkit.protocols import JSONLoader

        loader = JSONLoader('{"host": "localhost"}')
        assert hasattr(loader, "load")

    def test_json_loader_returns_dict(self):
        """JSONLoader.load() should return a parsed dictionary."""
        from configkit.protocols import JSONLoader

        loader = JSONLoader('{"host": "localhost", "port": 5432}')
        result = loader.load()
        assert result == {"host": "localhost", "port": 5432}

    def test_json_loader_satisfies_protocol(self):
        """JSONLoader should satisfy the Loadable protocol."""
        from configkit.protocols import JSONLoader, Loadable

        loader = JSONLoader('{"a": 1}')
        assert isinstance(loader, Loadable)
