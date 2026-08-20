import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from core.generator import UltimateExploitEngine
BANNER = """
 [bold red] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██████╗ ██████╗ ██████╗ ███████╗[/bold red]
 [bold red]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔══██╗██╔══██╗██╔══██╗██╔════╝[/bold red]
 [bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ██████╔╝██████╔╝██████╔╝███████╗[/bold white]
 [bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██╔═══╝ ██╔═══╝ ██╔═══╝ ╚════██║[/bold white]
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ██║     ██║     ██║     ███████║[/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝     ╚═╝     ╚═╝     ╚══════╝[/bold blue]
 [bold yellow]     Ultimate Exploit & Multi-Platform Encrypted Payload Framework (2026)[/bold yellow]
 [italic cyan]                               Ghost-SY1 Security[/italic cyan]
"""
console = Console()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    lhost = Prompt.ask("[bold yellow]Enter Listener LHOST[/bold yellow]")
    lport = int(Prompt.ask("[bold yellow]Enter Listener LPORT[/bold yellow]"))
    console.print("[bold cyan][1][/bold cyan] Buffer Overflow Exploit Generator (Stack Overwrite & NOP Sled)")
    console.print("[bold cyan][2][/bold cyan] Encrypted Multi-Platform Payloads (Windows C#, PowerShell, Linux, Android, macOS, iOS)")
    choice = Prompt.ask("[bold yellow]Select Exploitation Mode[/bold yellow]", choices=["1", "2"])
    engine = UltimateExploitEngine(lhost, lport)
    if choice == "1":
        offset = int(Prompt.ask("[bold yellow]Enter Buffer Offset (e.g. 512)[/bold yellow]", default="512"))
        target = Prompt.ask("[bold yellow]Enter Target IP[/bold yellow]", default="192.168.1.100")
        exploit_code = engine.generate_buffer_overflow_exploit(offset, target)
        syntax = Syntax(exploit_code, "python", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title="Buffer Overflow Exploit Script", border_style="bold red"))
    elif choice == "2":
        platform = Prompt.ask("[bold yellow]Target Platform[/bold yellow]", choices=["windows", "linux", "android", "macos", "ios"], default="windows")
        ptype = "powershell"
        if platform == "windows":
            ptype = Prompt.ask("[bold yellow]Payload Format[/bold yellow]", choices=["powershell", "csharp"], default="powershell")
        payload = engine.generate_encrypted_payload(platform, ptype)
        syntax = Syntax(payload, "csharp" if ptype=="csharp" else "powershell", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title=f"Encrypted Payload for {platform.upper()} ({ptype})", border_style="bold green"))
if __name__ == "__main__":
    main()
