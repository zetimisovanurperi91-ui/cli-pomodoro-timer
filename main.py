import time
from rich import print
from rich.panel import Panel
from rich.progress import BarColumn, Progress, TextColumn, TimeRemainingColumn

WORK_TIME = 25 * 60
REST_TIME = 5 * 60

def run_timer(duration: int, session_name: str):
    print(f"\n[bold cyan]🚀 Starting session: {session_name}[/bold cyan]")
    with Progress(
        TextColumn("[bold progress.description]{task.description}"),
        BarColumn(bar_width=40),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeRemainingColumn(),
    ) as progress:
        task = progress.add_task(f"[green]{session_name}...", total=duration)
        elapsed = 0
        while elapsed < duration:
            time.sleep(1)
            elapsed += 1
            progress.update(task, advance=1)

def main():
    session = 1
    try:
        while True:
            print(Panel.fit(f"[bold yellow]🍅 Pomodoro Timer — Session #{session}[/bold yellow]", border_style="magenta"))
            run_timer(WORK_TIME, "Focus Time")
            print("[bold green]✨ Time is up! Great job. Take a break! ☕[/bold green]")
            run_timer(REST_TIME, "Break Time")
            print("[bold blue]🔔 Break is over! Back to work. 💻[/bold blue]")
            session += 1
    except KeyboardInterrupt:
        print("\n\n[bold red]🛑 Timer stopped. Come back soon! 💪[/bold red]")

if __name__ == "__main__":
    main()