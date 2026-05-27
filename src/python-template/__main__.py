"""Template repository for creating extendable and modern python cli and gui applications"""

from .cli.app import main


def run() -> None:
    """Main entry point to the application."""
    # todo import main from cli/app and pass in sys.argv
    main()


if __name__ == "__main__":
    run()
