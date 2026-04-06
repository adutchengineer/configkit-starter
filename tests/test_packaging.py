"""Step 5: Package Structure

Tests for proper package organization — imports work, public API is exposed.
"""


class TestPackageImports:
    def test_import_config(self):
        """Config should be importable from the top-level package."""
        from configkit import Config

        config = Config({"a": 1})
        assert config.get("a") == 1

    def test_import_json_parser(self):
        """JSONParser should be importable from the top-level package."""
        from configkit import JSONParser

        parser = JSONParser()
        result = parser.parse('{"host": "localhost"}')
        assert result == {"host": "localhost"}

    def test_import_load_file(self):
        """load_file should be importable from the top-level package."""
        from configkit import load_file

        assert callable(load_file)
