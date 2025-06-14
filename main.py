import psutil
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Vertical
from textual.reactive import reactive

class CPUMemoryWidget(Static):
    cpu: reactive[float] = reactive(0.0)
    memory: reactive[float] = reactive(0.0)
    
    async def on_mount(self) -> None:
        self.set_interval(1, self.refresh_stats)
        
    def refresh_stats(self) -> None:
        self.cpu = psutil.cpu_percent()
        self.memory = psutil.virtual_memory().percent
    
    def render(self) -> str:
        return(
            f"💻  [bold green]CPU Usage:[/bold green] {self.cpu}%\n"
            f"📦  [bold cyan]Memory Usage:[/bold cyan] {self.memory}%"
        )
        
class MonitorApp(App):
    TITLE = "System Monitor"
    BINDNINGS = [("q", "quit", "Quit")]
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            CPUMemoryWidget(),
            Static("[dim]Updates every second - press 'q' to quit[/dim]")
        )
        yield Footer()
if __name__ == "__main__":
    MonitorApp().run()