"""
Entrypoint for the Norminette hook.
"""
from norminette.__main__ import main as entry_point


def main() -> None:
    """Forwards to the norminette entrypoint"""
    entry_point()


if __name__ == '__main__':
    raise SystemExit(main())
