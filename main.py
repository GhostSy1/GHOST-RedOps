import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from core.generator import StandaloneEliteEngine
BANNER = """
 [bold red] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██████╗ ██████╗ ██████╗ ███████╗[/bold red]
 [bold red]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔══██╗██╔══██╗██╔══██╗██╔════╝[/bold red]
 [bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ██████╔╝██████╔╝██████╔╝███████╗[/bold white]
 [bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██╔═══╝ ██╔═══╝ ██╔═══╝ ╚════██║[/bold white]
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ██║     ██║     ██║     ███████║[/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝     ╚═╝     ╚═╝     ╚══════╝[/bold blue]
 [bold yellow]         Standalone Elite C2 & Native Raw Shellcode Engine[/bold yellow]
 [italic cyan]                               Ghost-SY1 Security 2026[/italic cyan]
"""
console = Console()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    lhost = Prompt.ask("[bold yellow]Enter Standalone Listener LHOST[/bold yellow]")
    lport = int(Prompt.ask("[bold yellow]Enter Standalone Listener LPORT[/bold yellow]"))
    console.print("[bold cyan][1][/bold cyan] Polymorphic Python Stager (Standalone Obfuscation)")
    console.print("[bold cyan][2][/bold cyan] Raw Shellcode Generator (Hex & C-Array Native Generation)")
    console.print("[bold cyan][3][/bold cyan] Standalone Python C2 Listener Script (No Kali/Metasploit Needed)")
    choice = Prompt.ask("[bold yellow]Select Operation Mode[/bold yellow]", choices=["1", "2", "3"])
    engine = StandaloneEliteEngine(lhost, lport)
    if choice == "1":
        payload = engine.generate_polymorphic_python()
        syntax = Syntax(payload, "python", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title="Standalone Polymorphic Python Stager", border_style="bold green"))
    elif choice == "2":
        arch = Prompt.ask("[bold yellow]Architecture[/bold yellow]", choices=["x64", "x86"], default="x64")
        res = engine.generate_standalone_raw_shellcode(arch)
        console.print(Panel(f"[bold red]Raw Hex Shellcode:[/bold red]\n{res['hex']}", border_style="red"))
        console.print(Panel(f"[bold yellow]C-Array Shellcode Buffer:[/bold yellow]\n{{ {res['c_array']} }}", border_style="yellow"))
    elif choice == "3":
        listener = engine.generate_native_listener_script()
        syntax = Syntax(listener, "python", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title="Standalone Native C2 Listener", border_style="bold green"))
if __name__ == "__main__":
    main()
