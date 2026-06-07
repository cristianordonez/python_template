from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import argparse


class BaseCommand(ABC):
    name: str = ""
    help: str = ""

    def register(self, subparser: argparse._SubParsersAction) -> None:
        parser = subparser.add_parser(self.name, help=self.help)
        self.add_arguments(parser)
        parser.set_defaults(func=self.run)
        return parser

    @abstractmethod
    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        """Configure command arguments

        :param parser: ArgumentParser instance
        """

    @abstractmethod
    def run(self, args: argparse.Namespace) -> int:
        """Run the command"""


class CommandGroup(BaseCommand):
    """CLI command."""

    subcommands: list[BaseCommand] = []

    def register(self, subparser: argparse._SubParsersAction) -> None:
        """Register subcommands

        :param subparsers: Add subcommands to current command
        """
        parser = subparser.add_parser(self.name, help=self.help)
        self.add_arguments(parser)
        child_subparser = parser.add_subparsers(
            dest=f"{self.name}_command", required=True
        )
        for command in self.subcommands:
            command.register(child_subparser)

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        """Configure command arguments if necessary.

        :param parser: ArgumentParser instance
        """
        pass

    def run(self, args: argparse.Namespace) -> int:
        """Run the command"""
        raise NotImplementedError("Command Group not called")
