# configkit

Build a configuration management tool step by step. Each step applies concepts from the corresponding lesson in the [Software Design](https://dutchengineer.com/foundations/software-design/) module.

## Setup

```bash
uv sync --all-extras
uv run pytest tests/ -v
```

All tests start failing. As you complete each step, the corresponding tests will pass.

## Steps

| Step | Topic | Test file | Command |
|------|-------|-----------|---------|
| 1 | Config Class | `tests/test_config.py` | `uv run pytest tests/test_config.py` |
| 2 | Magic Methods | `tests/test_magic_methods.py` | `uv run pytest tests/test_magic_methods.py` |
| 3 | Loaders (Composition) | `tests/test_loaders.py` | `uv run pytest tests/test_loaders.py` |
| 4 | Package Structure | — | `uv pip install -e . && python -c "from configkit import Config"` |
| 5 | Testing | `tests/` | `uv run pytest --cov=configkit` |
| 6 | Logging | — | Commit and push |
| 7 | CLI | — | `uv pip install -e . && configkit validate config.json` |
| 8 | Docker | — | `docker build -t configkit .` |
| 9 | Docker Compose | — | `docker compose up` |

## Workflow

1. Read the step instructions on the [project page](https://dutchengineer.com/foundations/software-design/project-configkit/)
2. Implement the step
3. Run the tests for that step
4. Commit and push
5. CI runs all tests — green checks mean the step passes

## Project structure

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
