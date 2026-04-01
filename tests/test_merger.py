import pytest


class TestConfigMerger:
    def test_merge_two_configs(self):
        """Merging two configs should combine their keys.

        Later sources should override earlier ones for conflicting keys.
        """
        pytest.skip("Implement in Lesson 3")

    def test_merge_nested_configs(self):
        """Merging nested configs should deep-merge dictionaries.

        Example:
            base = Config({"database": {"host": "localhost", "port": 5432}})
            override = Config({"database": {"port": 5433}})
            merged = merge(base, override)
            assert merged.get("database.host") == "localhost"
            assert merged.get("database.port") == 5433
        """
        pytest.skip("Implement in Lesson 3")

    def test_merge_empty_config(self):
        """Merging with an empty config should return the original values."""
        pytest.skip("Implement in Lesson 3")
