import os
import sys
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from core.generator import AutonomousExploitEngine
from core.stealth import PhantomStealthEngine

BANNER = """
 [bold red] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██████╗ ██████╗ ██████╗ ███████╗[/bold red]
 [bold red]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔══██╗██╔══██╗██╔══██╗██╔════╝[/bold red]
 [bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ██████╔╝██████╔╝██████╔╝███████╗[/bold white]
 [bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██╔═══╝ ██╔═══╝ ██╔═══╝ ╚════██║[/bold white]
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ██║     ██║     ██║     ███████║[/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝     ╚═╝     ╚═╝     ╚══════╝[/bold blue]
 [bold yellow]     GHOST-RedOps: Elite Operating System Exploitation & C2 Suite[/bold yellow]
 [italic cyan]                               Ghost-SY1 Security[/italic cyan]
"""

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    console.print("[bold yellow][*] Initializing GHOST-RedOps System Exploitation Engine...[/bold yellow]\n")
    
    target_ip = Prompt.ask("[bold cyan]Enter Target System IP Address[/bold cyan]")
    lhost = Prompt.ask("[bold cyan]Enter Listener LHOST (Your IP)[/bold cyan]")
    lport = int(Prompt.ask("[bold cyan]Enter Listener LPORT (Port)[/bold cyan]"))
    
    stealth = PhantomStealthEngine()
    console.print(f"\n[bold green][*][/bold green] Engaging EDR Evasion & Memory Obfuscation...")
    stealth.evade_waf_delay()
    
    engine = AutonomousExploitEngine(lhost, lport, target_ip)
    auto_cve = engine.payload_db[0]['cve'] if engine.payload_db else "CVE-2026-0001"
    
    result = engine.execute_autonomous_exploit(auto_cve)
    
    if result["status"] == "success":
        console.print(Panel(f"[bold green]Target System Product:[/bold green] {result['product']}\n[bold cyan]Matched OS Exploit:[/bold cyan] {result['cve']} ({result['vulnerability_type']})\n[bold yellow]Stealth Mode:[/bold yellow] Active (Memory Injection Ready)", border_style="bold green"))
        
        syntax = Syntax(result['autonomous_script'], "python", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title=f"Weaponized OS Exploit Script for {result['cve']}", border_style="bold red"))
        console.print(f"\n[bold green][+][/bold green] Module Focus: [bold white]Operating System & System-Level Exploitation Only[/bold white]")
    else:
        console.print(f"[bold red][!][/bold red] {result['message']}")

if __name__ == "__main__":
    main()
