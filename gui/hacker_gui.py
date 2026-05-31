import textual
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, DataTable, Log
from textual.containers import Horizontal, Vertical

class AETHERHackerGUI(App):
    """Hacker-style TUI for AETHER-1"""
    CSS_PATH = "hacker_theme.css"

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal():
            with Vertical():
                yield Static("[bold green]LIVE STATUS[/]", id="status")
                yield DataTable(id="memory")
            with Vertical():
                yield Static("[bold cyan]WORLD MODEL[/]")
                yield Log(id="world_model")
        yield Footer()

    def on_mount(self):
        self.title = "AETHER-1 :: LIVING ENTITY v1.0"
        # Populate with live data from core

if __name__ == "__main__":
    AETHERHackerGUI().run()