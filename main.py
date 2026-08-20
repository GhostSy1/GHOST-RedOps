import os
import sys
import time
import json
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
 [bold yellow]     GHOST-RedOps: Elite Weaponized Exploit Engine & 1100+ Active DB[/bold yellow]
 [italic cyan]                               Ghost-SY1 Security[/italic cyan]
"""

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_help():
    help_text = """
[bold yellow]GHOST-RedOps Help Menu[/bold yellow]

[bold cyan]Description:[/bold cyan]
Advanced Red Team framework for autonomous exploitation and payload delivery.

[bold cyan]Options:[/bold cyan]
1. [bold white]Target IP[/bold white]: Specify the IP address of the target system.
2. [bold white]LHOST[/bold white]: Your listener IP for reverse connections.
3. [bold white]LPORT[/bold white]: Your listener port for reverse connections.
4. [bold white]Autonomous Mode[/bold white]: Automatically matches services with 1100+ CVEs.

[bold cyan]Usage:[/bold cyan]
Follow the interactive prompts after startup to configure your engagement.
"""
    console.print(Panel(help_text, title="Help & Documentation", border_style="blue"))

def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        show_help()
        return

    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    
    # Explicit Database Check
    db_path = os.path.join(os.path.dirname(__file__), 'db/payloads.json')
    if os.path.exists(db_path):
        with open(db_path, 'r') as f:
            db_size = len(json.load(f))
        console.print(f"[bold green][*] Successfully loaded weaponized database with {db_size} active exploits.[/bold green]")
    else:
        console.print("[bold red][!] Warning: Exploit database not found![/bold red]")

    console.print("[bold yellow][*] Initializing Ghost-RedOps Elite Weaponized Engine...[/bold yellow]\n")
    
    target_ip = Prompt.ask("[bold cyan]Enter Target System IP[/bold cyan]")
    lhost = Prompt.ask("[bold cyan]Enter Listener LHOST (Your IP)[/bold cyan]")
    lport = int(Prompt.ask("[bold cyan]Enter Listener LPORT (Port)[/bold cyan]"))
    
    stealth = PhantomStealthEngine()
    console.print(f"\n[bold green][*][/bold green] Engaging Anti-Ban Stealth & Memory Obfuscation...")
    stealth.evade_waf_delay()
    
    engine = AutonomousExploitEngine(lhost, lport, target_ip)
    auto_cve = engine.payload_db[0]['cve'] if engine.payload_db else "CVE-2026-0001"
    
    match = next((v for v in engine.payload_db if v['cve'] == auto_cve), engine.payload_db[0])
    
    console.print(Panel(
        f"[bold green]Target Product:[/bold green] {match['product']}\n"
        f"[bold cyan]Matched Exploit:[/bold cyan] {match['cve']} ({match['vulnerability_type']})\n"
        f"[bold yellow]Reliability Score:[/bold yellow] [bold green]{match['reliability_score']}/10[/bold green]\n"
        f"[bold white]Verification Steps:[/bold white] {match['verification_steps']}",
        title="[bold red]Elite Exploit Selection[/bold red]",
        border_style="bold red"
    ))
    
    result = engine.execute_autonomous_exploit(match['cve'])
    
    if result["status"] == "success":
        syntax = Syntax(result['autonomous_script'], "python", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title=f"Weaponized Payload for {match['cve']}", border_style="bold red"))
        console.print(f"\n[bold green][+][/bold green] Status: [bold white]Payload Weaponized & Ready for Injection[/bold white]")
    else:
        console.print(f"[bold red][!][/bold red] {result['message']}")

if __name__ == "__main__":
    main()
