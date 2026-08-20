import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.syntax import Syntax
from core.generator import UltimateExploitEngine

BANNER = """
 [bold red] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██████╗ ██████╗ ██████╗ ███████╗[/bold red]
 [bold red]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔══██╗██╔══██╗██╔══██╗██╔════╝[/bold red]
 [bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ██████╔╝██████╔╝██████╔╝███████╗[/bold white]
 [bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██╔═══╝ ██╔═══╝ ██╔═══╝ ╚════██║[/bold white]
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ██║     ██║     ██║     ███████║[/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝     ╚═╝     ╚═╝     ╚══════╝[/bold blue]
 [bold yellow]     Ultimate Red Ops & 1000+ CVE Exploit Encyclopedia (2026)[/bold yellow]
 [italic cyan]                               Ghost-SY1 Security[/italic cyan]
"""

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    
    console.print("[bold yellow][*] Initializing Ghost-RedOps Encyclopedia...[/bold yellow]\n")
    lhost = Prompt.ask("[bold cyan]Enter Listener LHOST (IP)[/bold cyan]")
    lport = int(Prompt.ask("[bold cyan]Enter Listener LPORT (Port)[/bold cyan]"))
    
    engine = UltimateExploitEngine(lhost, lport)
    
    console.print("\n[bold green]Encyclopedia Options:[/bold green]")
    console.print("[bold cyan][1][/bold cyan] Search & Generate Exploit by CVE ID (1000+ DB)")
    console.print("[bold cyan][2][/bold cyan] List Latest Critical Exploits (2024-2026)")
    console.print("[bold cyan][3][/bold cyan] Multi-Platform Stager Generator")
    
    choice = Prompt.ask("[bold yellow]Select Option[/bold yellow]", choices=["1", "2", "3"])
    
    if choice == "1":
        cve_id = Prompt.ask("[bold yellow]Enter CVE ID (e.g. CVE-2026-1234)[/bold yellow]")
        exploit = engine.generate_custom_exploit(cve_id)
        console.print(Panel(exploit, title=f"Ghost-SY1 Exploit for {cve_id}", border_style="bold red"))
    
    elif choice == "2":
        exploits = engine.get_top_exploits()
        t = Table(title="Top 10 Critical Exploits in Database", border_style="bold red")
        t.add_column("CVE ID", style="cyan")
        t.add_column("Product", style="white")
        t.add_column("Severity", style="bold red")
        for e in exploits:
            t.add_row(e['cve'], e['product'], e['severity'])
        console.print(t)
        
    elif choice == "3":
        console.print("[bold yellow][*] Redirecting to Multi-Platform Engine...[/bold yellow]")
        # (Simplified for this update)

if __name__ == "__main__":
    main()
