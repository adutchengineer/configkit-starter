"""Step 9: CLI

Tests for the configkit CLI — validate, diff, and merge commands.
"""

import json
import tempfile
import os


class TestCLIValidate:
    def test_validate_import(self):
        """The CLI module should be importable."""
        from configkit import cli

        assert hasattr(cli, "app")

    def test_validate_valid_config(self):
        """validate command should succeed on a valid config file."""
        from typer.testing import CliRunner
        from configkit.cli import app

        runner = CliRunner()
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            json.dump({"host": "localhost", "port": 5432}, f)
            f.flush()
            result = runner.invoke(app, ["validate", f.name])
            assert result.exit_code == 0
            os.unlink(f.name)


class TestCLIDiff:
    def test_diff_identical_files(self):
        """diff command should show no differences for identical files."""
        from typer.testing import CliRunner
        from configkit.cli import app

        runner = CliRunner()
        data = {"host": "localhost", "port": 5432}
        files = []
        for _ in range(2):
            f = tempfile.NamedTemporaryFile(
                mode="w", suffix=".json", delete=False
            )
            json.dump(data, f)
            f.flush()
            files.append(f.name)
            f.close()

        result = runner.invoke(app, ["diff", files[0], files[1]])
        assert result.exit_code == 0
        for f in files:
            os.unlink(f)


class TestCLIMerge:
    def test_merge_two_files(self):
        """merge command should combine two config files."""
        from typer.testing import CliRunner
        from configkit.cli import app

        runner = CliRunner()
        files = []
        for data in [{"host": "localhost"}, {"port": 5432}]:
            f = tempfile.NamedTemporaryFile(
                mode="w", suffix=".json", delete=False
            )
            json.dump(data, f)
            f.flush()
            files.append(f.name)
            f.close()

        result = runner.invoke(app, ["merge"] + files)
        assert result.exit_code == 0
        for f in files:
            os.unlink(f)
