"""
Metadata Scrubber Tool - CLI Application Entry Point.

This module serves as the main entry point for the CLI application.
It initializes the Typer app, registers commands, and configures logging.

Commands:
    read: Display metadata from files.
    scrub: Remove metadata from files.
"""

import logging

import typer

from src.commands.read import read
from src.commands.scrub import scrub
from src.utils.logger import setup_logging

# Initialize the Typer app with helpful defaults
app = typer.Typer(no_args_is_help=True, pretty_exceptions_show_locals=False)
log = logging.getLogger("metadata-scrubber")


__version__ = "0.2.0"


# ---------------------------------------------------------
# VERSION CALLBACK
# ---------------------------------------------------------
def version_callback(value: bool):
    """
    Prints the version and exits.
    """
    if value:
        print(f"Version: {__version__}")
        raise typer.Exit()


# ---------------------------------------------------------
# MAIN ENTRY POINT
# ---------------------------------------------------------
# fmt: off
@app.callback()
def main(
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-V",
        help="Show detailed debug logs for every file processed.",
    ),
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show the application version and exit."
    ),
):
    """
    Metadata Scrubber Tool - Clean your images personal identifying data. eg: author name, camera model, GPS coordinates, etc.
    """
    # Initialize the logger based on the user's flag
    setup_logging(verbose)

    if verbose:
        log.debug("🐛 Verbose mode enabled. Detailed logs active.")
# fmt: on

# register commands
app.command(name="read")(read)
app.command(name="scrub")(scrub)

# run app
if __name__ == "__main__":
    app()
