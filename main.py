import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from core.generator import UltimateRedOpsEngine
BANNER = """
 [bold red] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██████╗ ██████╗ ██████╗ ███████╗[/bold red]
 [bold red]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔══██╗██╔══██╗██╔══██╗██╔════╝[/bold red]
 [bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ██████╔╝██████╔╝██████╔╝███████╗[/bold white]
 [bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██╔═══╝ ██╔═══╝ ██╔═══╝ ╚════██║[/bold white]
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ██║     ██║     ██║     ███████║[/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝     ╚═╝     ╚═╝     ╚══════╝[/bold blue]
 [bold yellow]         Ultimate Red Ops & Multi-Vector Exploitation Framework (2026)[/bold yellow]
 [italic cyan]                               Ghost-SY1 Security[/italic cyan]
"""
console = Console()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    console.print("[bold yellow][*] Initializing Ghost-RedOps Interactive Engine...[/bold yellow]\n")
    lhost = Prompt.ask("[bold cyan]Enter Listener LHOST (IP)[/bold cyan]")
    lport = int(Prompt.ask("[bold cyan]Enter Listener LPORT (Port)[/bold cyan]"))
    console.print("\n[bold green]Select Exploitation Vector:[/bold green]")
    console.print("[bold cyan][1][/bold cyan] DLL Side-Loading Exploit Template (C++)")
    console.print("[bold cyan][2][/bold cyan] HTA Web Attack Vector (ActiveX / PowerShell Stager)")
    console.print("[bold cyan][3][/bold cyan] VBA Macro Payload (Office Social Engineering)")
    choice = Prompt.ask("[bold yellow]Select Option[/bold yellow]", choices=["1", "2", "3"])
    engine = UltimateRedOpsEngine(lhost, lport)
    if choice == "1":
        payload = engine.generate_dll_side_loading()
        syntax = Syntax(payload, "cpp", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title="DLL Side-Loading Template", border_style="bold red"))
    elif choice == "2":
        payload = engine.generate_hta_attack()
        syntax = Syntax(payload, "html", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title="HTA Attack Vector", border_style="bold red"))
    elif choice == "3":
        payload = engine.generate_macro_payload()
        syntax = Syntax(payload, "vbnet", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title="VBA Macro Payload", border_style="bold red"))
if __name__ == "__main__":
    main()
