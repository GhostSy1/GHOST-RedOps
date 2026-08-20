import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from core.orchestrator import MasterOrchestrator

BANNER = """
 [bold red] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██████╗ ██████╗ ██████╗ ███████╗[/bold red]
 [bold red]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔══██╗██╔══██╗██╔══██╗██╔════╝[/bold red]
 [bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ██████╔╝██████╔╝██████╔╝███████╗[/bold white]
 [bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██╔═══╝ ██╔═══╝ ██╔═══╝ ╚════██║[/bold white]
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ██║     ██║     ██║     ███████║[/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝     ╚═╝     ╚═╝     ╚══════╝[/bold blue]
 [bold yellow]     Master Orchestrator: Zero-Input Autonomous Exploit Engine (2026)[/bold yellow]
 [italic cyan]                               Ghost-SY1 Security[/italic cyan]
"""

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    
    console.print("[bold yellow][*] Initializing Ghost-SY1 Master Orchestrator...[/bold yellow]\n")
    
    # User inputs only Target and Listener info as requested
    target = Prompt.ask("[bold cyan]Enter Target (URL/Domain for Web or IP for Network)[/bold cyan]")
    lhost = Prompt.ask("[bold cyan]Enter Listener LHOST (Your IP)[/bold cyan]")
    lport = int(Prompt.ask("[bold cyan]Enter Listener LPORT (Port)[/bold cyan]"))
    
    console.print(f"\n[bold green][*][/bold green] Analyzing target [bold cyan]{target}[/bold cyan] and running Master Orchestration...")
    
    orchestrator = MasterOrchestrator(target, lhost, lport)
    result = orchestrator.execute_smart_orchestration()
    
    console.print(Panel(f"[bold green]Target Classification:[/bold green] {result['type']}\n[bold cyan]Auto-Matched CVE:[/bold cyan] {result['cve']}\n[bold yellow]Stealth Mode:[/bold yellow] Active (Proxy Rotation & WAF Evasion Enabled)", border_style="bold green"))
    
    syntax = Syntax(result['script'], "python", theme="monokai", line_numbers=True)
    console.print(Panel(syntax, title=f"Fully Autonomous Master Exploit Script ({result['type']})", border_style="bold red"))
    console.print(f"\n[bold green][+][/bold green] Execution Mode: [bold white]Zero Manual CVE Input / 100% Autonomous[/bold white]")

if __name__ == "__main__":
    main()
