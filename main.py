import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.syntax import Syntax
from core.generator import ActiveExploitEngine

BANNER = """
 [bold red] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██████╗ ██████╗ ██████╗ ███████╗[/bold red]
 [bold red]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔══██╗██╔══██╗██╔══██╗██╔════╝[/bold red]
 [bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ██████╔╝██████╔╝██████╔╝███████╗[/bold white]
 [bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██╔═══╝ ██╔═══╝ ██╔═══╝ ╚════██║[/bold white]
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ██║     ██║     ██║     ███████║[/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝     ╚═╝     ╚═╝     ╚══════╝[/bold blue]
 [bold yellow]     Active Exploit Generator & 1600+ CVE Active Arsenal (2026)[/bold yellow]
 [italic cyan]                               Ghost-SY1 Security[/italic cyan]
"""

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    
    console.print("[bold yellow][*] Initializing Ghost-RedOps Active Exploit Engine...[/bold yellow]\n")
    lhost = Prompt.ask("[bold cyan]Enter Listener LHOST (IP)[/bold cyan]")
    lport = int(Prompt.ask("[bold cyan]Enter Listener LPORT (Port)[/bold cyan]"))
    
    engine = ActiveExploitEngine(lhost, lport)
    
    cve_id = Prompt.ask("[bold yellow]Enter Target CVE ID to Exploit (e.g. CVE-2026-XXXX)[/bold yellow]")
    
    result = engine.get_exploit_by_cve(cve_id)
    if result:
        console.print(Panel(f"[bold green]Target Product:[/bold green] {result['product']}\n[bold cyan]Vulnerability Type:[/bold cyan] {result['vulnerability_type']}\n[bold yellow]Description:[/bold yellow] {result['description']}", border_style="bold green"))
        
        syntax = Syntax(result['custom_exploit'], "python", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title=f"Active Exploit Code for {result['cve']}", border_style="bold red"))
        console.print(f"\n[bold green][+][/bold green] Usage Type: [bold white]{result['usage_type']}[/bold white]")
    else:
        console.print(f"[bold red][!][/bold red] CVE ID '{cve_id}' not found in active local arsenal.")

if __name__ == "__main__":
    main()
