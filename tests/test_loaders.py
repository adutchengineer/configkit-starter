import pytest


class TestJSONLoader:
    def test_load_json_file(self):
        """JSONLoader should parse a .json file into a Config object."""
        pytest.skip("Implement in Lesson 3")

    def test_load_json_invalid(self):
        """JSONLoader should raise a clear error for malformed JSON."""
        pytest.skip("Implement in Lesson 3")


class TestYAMLLoader:
    def test_load_yaml_file(self):
        """YAMLLoader should parse a .yaml file into a Config object."""
        pytest.skip("Implement in Lesson 3")

    def test_load_yaml_invalid(self):
        """YAMLLoader should raise a clear error for malformed YAML."""
        pytest.skip("Implement in Lesson 3")


class TestEnvLoader:
    def test_load_env_vars(self):
        """EnvLoader should read prefixed environment variables into a Config.

        Example:
            With APP_DATABASE_HOST=localhost in env and prefix="APP_",
            the resulting Config should have {"database": {"host": "localhost"}}.
        """
        pytest.skip("Implement in Lesson 3")

    def test_load_env_no_prefix(self):
        """EnvLoader with no prefix should raise ValueError."""
        pytest.skip("Implement in Lesson 3")
