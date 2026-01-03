import typer
from rich.console import Console
from rich.panel import Panel

# Initialize the app and the console
app = typer.Typer()
console = Console()


@app.command()
def hello(name: str, formal: bool = False):
    """
    Say hello to a user.
    If --formal is used, it greets more politely.
    """
    if formal:
        message = (
            f"Good day to you, [bold magenta]{name}[/bold magenta]. It is a pleasure."
        )
        color = "green"
    else:
        message = f"Yo [bold cyan]{name}[/bold cyan]! What's up?"
        color = "yellow"

    # Use Rich to print a pretty panel instead of a boring print()
    console.print(Panel(message, title="Greeting System", style=color))


@app.command()
def goodbye(name: str):
    """
    Say goodbye.
    """
    console.print(f"[red]Goodbye, {name}![/red] 👋")


if __name__ == "__main__":
    app()
