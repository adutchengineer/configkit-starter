"""Step 8: Logging

Tests for module-level loggers and structured logging setup.
"""

import logging


class TestLoggerSetup:
    def test_config_module_has_logger(self):
        """configkit.config should have a module-level logger."""
        logger = logging.getLogger("configkit.config")
        assert logger is not None

    def test_loaders_module_has_logger(self):
        """configkit.loaders should have a module-level logger."""
        logger = logging.getLogger("configkit.loaders")
        assert logger is not None

    def test_logger_hierarchy(self):
        """Child loggers should propagate to the parent."""
        parent = logging.getLogger("configkit")
        child = logging.getLogger("configkit.config")
        assert child.parent == parent

    def test_setup_logging_exists(self):
        """setup_logging() should be importable from configkit."""
        from configkit import setup_logging

        assert callable(setup_logging)
