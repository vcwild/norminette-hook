# Norminette Hook

The Norminette pre-commit hook.

## Usage

Create a `.pre-commit-config.yaml` file in the root of your repository.

Add there the following lines:

```yaml
default_language_version:
  python: python3

repos:
  - repo: https://github.com/vcwild/norminette-hook
    rev: main
    hooks:
    - id: norminette-hook
```
