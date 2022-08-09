# Norminette Hook

The Norminette pre-commit hook.

## Usage

Create a `.pre-commit-config.yaml` file in the root of your repository.

Add there the following lines:

```yaml
- repo: https://github.com/vcwild/norminette-hook
  rev: v0.1.0
  hooks:
  - id: norminette-hook
```
