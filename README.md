# Norminette Hook

The Norminette pre-commit hook.

## Requirements

- [Pre-commit](https://pre-commit.com/index.html) must be installed on the system or in the repository virtual environment.

## Usage

Create a `.pre-commit-config.yaml` file in the root of your repository.

Add there the following lines:

```yaml
default_language_version:
  python: python3

repos:
  - repo: https://github.com/vcwild/norminette-hook
    rev: v0.1.0
    hooks:
    - id: norminette-hook
```

When executing `pre-commit run` or `pre-commit run norminette-hook`, the hook will be executed.
