"""Main entry point for cli"""

from __future__ import annotations

import sys


def main(args: list[str] | None = None) -> None:
    """Main entry point to CLI portion of application"""
    if args is None:
        args: list[str] = sys.argv[1:]
    print(f"Python template app started with args {args}")


if __name__ == "__main__":
    main()
