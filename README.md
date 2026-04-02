# configkit

A configuration management tool you will build step by step through the [Software Design](https://dutchengineer.com/foundations/software-design/) module. Each step applies concepts from the corresponding lesson — classes, composition, packaging, testing, and containerization.

## Getting started

```bash
uv sync --all-extras
uv run pytest tests/ -v
```

Every test starts failing. As you complete each step, the matching tests turn green.

## How it works

The [project page](https://dutchengineer.com/foundations/software-design/project-configkit/) walks you through 9 steps. After each step, run the tests, commit, and push. CI validates your work automatically — green checks mean the step passes.

**Step 1 — Config Class** builds the core `Config` class with dot-notation access and validation. Run `uv run pytest tests/test_config.py` to check your work.

**Step 2 — Magic Methods** adds `__repr__`, `__getitem__`, `__contains__`, and other dunder methods so `Config` behaves like a native Python object. Run `uv run pytest tests/test_magic_methods.py`.

**Step 3 — Loaders** introduces the Protocol pattern with JSON, YAML, and Env parsers. Run `uv run pytest tests/test_loaders.py`.

**Step 4 — Package Structure** organizes the code into a proper src layout with `__init__.py` and `pyproject.toml`. Verify with `uv pip install -e .` and `python -c "from configkit import Config"`.

**Step 5 — Testing** adds fixtures, parametrized tests, and mocking for comprehensive coverage. Run `uv run pytest --cov=configkit`.

**Step 6 — Logging** adds module loggers with DEBUG, INFO, and WARNING levels across the codebase.

**Step 7 — CLI** turns configkit into a command-line tool with `validate`, `diff`, and `merge` commands using typer.

**Step 8 — Docker** containerizes configkit with a multi-stage Dockerfile.

**Step 9 — Docker Compose** adds PostgreSQL and Redis alongside configkit for config versioning and caching.

## Project structure

As you work through the steps, you will create these files:

```
src/configkit/
├── __init__.py      # Re-exports (Step 4)
├── config.py        # Config class (Steps 1-2)
├── loaders.py       # Parsers + load_file (Step 3)
└── cli.py           # CLI commands (Step 7)
tests/
├── conftest.py      # Fixtures (Step 5)
├── test_config.py   # Step 1 tests
├── test_magic_methods.py  # Step 2 tests
└── test_loaders.py  # Step 3 tests
```
