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
 [bold yellow]         Advanced Red Team Operations & Meterpreter C2 Framework[/bold yellow]
 [italic cyan]                               Ghost-SY1 Security 2026[/italic cyan]
"""
console = Console()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    lhost = Prompt.ask("[bold yellow]Enter LHOST (Listener IP / Kali IP)[/bold yellow]")
    lport = int(Prompt.ask("[bold yellow]Enter LPORT (Listener Port)[/bold yellow]"))
    console.print("[bold cyan][1][/bold cyan] Python Polymorphic Reverse Shell")
    console.print("[bold cyan][2][/bold cyan] PowerShell Encoded Stager (EDR Bypass)")
    console.print("[bold cyan][3][/bold cyan] Meterpreter C2 (Windows / Linux / Android)")
    choice = Prompt.ask("[bold yellow]Select Operation Mode[/bold yellow]", choices=["1", "2", "3"])
    gen = PayloadGenerator(lhost, lport)
    if choice == "1":
        payload = gen.generate_python_payload()
        syntax = Syntax(payload, "python", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title="Generated Python Payload", border_style="bold green"))
    elif choice == "2":
        payload = gen.generate_powershell_payload()
        syntax = Syntax(payload, "powershell", theme="monokai", line_numbers=False)
        console.print(Panel(syntax, title="Generated PowerShell Stager", border_style="bold green"))
    elif choice == "3":
        os_target = Prompt.ask("[bold yellow]Target OS[/bold yellow]", choices=["windows", "linux", "android"], default="windows")
        cmd = gen.generate_meterpreter_command(os_target)
        handler = gen.get_msf_handler_config(os_target)
        console.print(Panel(f"[bold red]Msfvenom Generation Command:[/bold red]\n{cmd}", border_style="red"))
        console.print(Panel(f"[bold green]Metasploit Multi-Handler Configuration (Resource Script):[/bold green]\n{handler}", border_style="green"))
if __name__ == "__main__":
    main()
