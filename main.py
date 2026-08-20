import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from core.generator import PayloadGenerator
BANNER = """
 [bold red] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██████╗ ██████╗ ██████╗ ███████╗[/bold red]
 [bold red]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔══██╗██╔══██╗██╔══██╗██╔════╝[/bold red]
 [bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ██████╔╝██████╔╝██████╔╝███████╗[/bold white]
 [bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██╔═══╝ ██╔═══╝ ██╔═══╝ ╚════██║[/bold white]
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ██║     ██║     ██║     ███████║[/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝     ╚═╝     ╚═╝     ╚══════╝[/bold blue]
 [bold yellow]         Advanced Red Team Operations & Obfuscated Payload Generator[/bold yellow]
 [italic cyan]                               Ghost-SY1 Security 2026[/italic cyan]
"""
console = Console()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    lhost = Prompt.ask("[bold yellow]Enter LHOST (Listener IP)[/bold yellow]")
    lport = int(Prompt.ask("[bold yellow]Enter LPORT (Listener Port)[/bold yellow]"))
    console.print("[bold cyan][1][/bold cyan] Python Reverse Shell (Base64 Polymorphic)")
    console.print("[bold cyan][2][/bold cyan] PowerShell Encoded Stager (EDR Bypass)")
    choice = Prompt.ask("[bold yellow]Select Payload Type[/bold yellow]", choices=["1", "2"])
    gen = PayloadGenerator(lhost, lport)
    if choice == "1":
        payload = gen.generate_python_payload()
        syntax = Syntax(payload, "python", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title="Generated Python Payload", border_style="bold green"))
    elif choice == "2":
        payload = gen.generate_powershell_payload()
        syntax = Syntax(payload, "powershell", theme="monokai", line_numbers=False)
        console.print(Panel(syntax, title="Generated PowerShell Stager", border_style="bold green"))
if __name__ == "__main__":
    main()
