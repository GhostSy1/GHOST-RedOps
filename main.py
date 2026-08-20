import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.syntax import Syntax
from core.generator import AutonomousExploitEngine

BANNER = """
 [bold red] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██████╗ ██████╗ ██████╗ ███████╗[/bold red]
 [bold red]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔══██╗██╔══██╗██╔══██╗██╔════╝[/bold red]
 [bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ██████╔╝██████╔╝██████╔╝███████╗[/bold white]
 [bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██╔═══╝ ██╔═══╝ ██╔═══╝ ╚════██║[/bold white]
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ██║     ██║     ██║     ███████║[/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝     ╚═╝     ╚═╝     ╚══════╝[/bold blue]
 [bold yellow]     Autonomous Smart Exploit Engine & 1600+ CVE Arsenal (2026)[/bold yellow]
 [italic cyan]                               Ghost-SY1 Security[/italic cyan]
"""

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    
    console.print("[bold yellow][*] Initializing Ghost-RedOps Autonomous Framework...[/bold yellow]\n")
    
    # Prompt user for parameters after startup as requested
    target_ip = Prompt.ask("[bold cyan]Enter Target IP Address[/bold cyan]")
    lhost = Prompt.ask("[bold cyan]Enter Listener LHOST (Your IP)[/bold cyan]")
    lport = int(Prompt.ask("[bold cyan]Enter Listener LPORT (Port)[/bold cyan]"))
    cve_id = Prompt.ask("[bold cyan]Enter Target CVE ID (e.g. CVE-2026-XXXX)[/bold cyan]")
    
    console.print(f"\n[bold green][*][/bold green] Engaging autonomous engine for target [bold cyan]{target_ip}[/bold cyan] using [bold yellow]{cve_id}[/bold yellow]...")
    
    engine = AutonomousExploitEngine(lhost, lport, target_ip)
    result = engine.execute_autonomous_exploit(cve_id)
    
    if result["status"] == "success":
        console.print(Panel(f"[bold green]Target Product:[/bold green] {result['product']}\n[bold cyan]Detected Vulnerability Type:[/bold cyan] {result['vulnerability_type']}\n[bold yellow]Status:[/bold yellow] Payload Auto-Selected & Configured Successfully", border_style="bold green"))
        
        syntax = Syntax(result['autonomous_script'], "python", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title=f"Autonomous Weaponized Exploit Script for {result['cve']}", border_style="bold red"))
        console.print(f"\n[bold green][+][/bold green] Execution Mode: [bold white]Fully Autonomous Active Exploitation[/bold white]")
    else:
        console.print(f"[bold red][!][/bold red] {result['message']}")

if __name__ == "__main__":
    main()
