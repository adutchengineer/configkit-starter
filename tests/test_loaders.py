"""Step 3: Loaders (Composition)

Tests for the Protocol-based parser pattern — JSON, YAML, and Env parsers,
plus file loading and the parser registry.
"""

import json
import os
import tempfile

import pytest


class TestJSONParser:
    def test_parse_valid_json(self):
        """JSONParser.parse should return a dict from a JSON string."""
        from configkit.loaders import JSONParser

        result = JSONParser().parse('{"host": "localhost", "port": 5432}')
        assert result == {"host": "localhost", "port": 5432}

    def test_parse_invalid_json(self):
        """JSONParser.parse should raise on malformed JSON."""
        from configkit.loaders import JSONParser

        with pytest.raises(Exception):
            JSONParser().parse("{bad json}")


class TestYAMLParser:
    def test_parse_valid_yaml(self):
        """YAMLParser.parse should return a dict from a YAML string."""
        from configkit.loaders import YAMLParser

        result = YAMLParser().parse("host: localhost\nport: 5432\n")
        assert result == {"host": "localhost", "port": 5432}

    def test_parse_invalid_yaml(self):
        """YAMLParser.parse should raise on malformed YAML."""
        from configkit.loaders import YAMLParser

        with pytest.raises(Exception):
            YAMLParser().parse(":\n  :\n    - :")


class TestEnvParser:
    def test_parse_key_value_lines(self):
        """EnvParser should parse KEY=VALUE lines into a dict."""
        from configkit.loaders import EnvParser

        content = "HOST=localhost\nPORT=5432\n"
        result = EnvParser().parse(content)
        assert result["HOST"] == "localhost"
        assert result["PORT"] == "5432"

    def test_parse_nested_via_double_underscore(self):
        """EnvParser should convert __ separators into nested dicts."""
        from configkit.loaders import EnvParser

        content = "DATABASE__HOST=localhost\nDATABASE__PORT=5432\n"
        result = EnvParser().parse(content)
        assert result == {"DATABASE": {"HOST": "localhost", "PORT": "5432"}}


class TestLoadFile:
    def test_load_json_file(self):
        """load_file should read a file and parse it with the given parser."""
        from configkit.loaders import JSONParser, load_file

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            json.dump({"key": "value"}, f)
            f.flush()
            path = f.name

        try:
            result = load_file(path, JSONParser())
            assert result == {"key": "value"}
        finally:
            os.unlink(path)


class TestParserRegistry:
    def test_registry_has_json(self):
        """PARSERS dict should map '.json' to a JSONParser instance."""
        from configkit.loaders import PARSERS

        assert ".json" in PARSERS

    def test_registry_has_yaml(self):
        """PARSERS dict should map '.yaml' to a YAMLParser instance."""
        from configkit.loaders import PARSERS

        assert ".yaml" in PARSERS
