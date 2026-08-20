import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from core.generator import MultiPlatformEliteEngine
BANNER = """
 [bold red] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██████╗ ██████╗ ██████╗ ███████╗[/bold red]
 [bold red]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔══██╗██╔══██╗██╔══██╗██╔════╝[/bold red]
 [bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ██████╔╝██████╔╝██████╔╝███████╗[/bold white]
 [bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██╔═══╝ ██╔═══╝ ██╔═══╝ ╚════██║[/bold white]
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ██║     ██║     ██║     ███████║[/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝     ╚═╝     ╚═╝     ╚══════╝[/bold blue]
 [bold yellow]     Multi-Platform Elite C2 & Polymorphic Payload Generator (2026)[/bold yellow]
 [italic cyan]                               Ghost-SY1 Security[/italic cyan]
"""
console = Console()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    lhost = Prompt.ask("[bold yellow]Enter Listener LHOST[/bold yellow]")
    lport = int(Prompt.ask("[bold yellow]Enter Listener LPORT[/bold yellow]"))
    console.print("[bold cyan][1][/bold cyan] Windows (PowerShell Encoded Stager)")
    console.print("[bold cyan][2][/bold cyan] Linux (Polymorphic Python Reverse Shell)")
    console.print("[bold cyan][3][/bold cyan] Android (Meterpreter APK Generator Command)")
    console.print("[bold cyan][4][/bold cyan] macOS (Obfuscated Zsh/Python Stager)")
    console.print("[bold cyan][5][/bold cyan] iOS / iPhone (Base64 Encoded Sh Stager)")
    choice = Prompt.ask("[bold yellow]Select Target Operating System[/bold yellow]", choices=["1", "2", "3", "4", "5"])
    platforms = {"1": "windows", "2": "linux", "3": "android", "4": "macos", "5": "ios"}
    target_os = platforms.get(choice, "windows")
    engine = MultiPlatformEliteEngine(lhost, lport)
    payload = engine.generate_payload(target_os)
    if target_os == "android":
        console.print(Panel(f"[bold red]Android Generation Command:[/bold red]\n{payload}", border_style="red"))
    else:
        syntax = Syntax(payload, "bash" if target_os in ["linux", "ios", "macos"] else "powershell", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title=f"Elite Payload for {target_os.upper()}", border_style="bold green"))
if __name__ == "__main__":
    main()
