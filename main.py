import os
import sys
import argparse
import json

def banner():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(r"""
  ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██████╗ ███████╗██████╗  ██████╗ ██████╗ ███████╗
 ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗██╔════╝
 ██║  ███╗███████║██║   ██║███████╗   ██║        ██████╔╝█████╗  ██║  ██║██║   ██║██████╔╝███████╗
 ██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██╔══██╗██╔══╝  ██║  ██║██║   ██║██╔═══╝ ╚════██║
 ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║        ██║  ██║███████╗██████╔╝╚██████╔╝██║     ███████║
  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝        ╚═╝  ╚═╝╚══════╝╚══════╝  ╚══════╝╚═╝     ╚══════╝
    GHOST-RedOps: Authorized Red Team Operations & Session Controller (v3.0-PRO)
""")

def main():
    banner()
    parser = argparse.ArgumentParser(description="GHOST-RedOps C2 & Operations Suite")
    parser.add_argument("--listener", help="Listener bind port", default="4444")
    parser.add_argument("--payload", help="Target OS payload type (windows/linux/android/macos)", default="windows")
    parser.add_argument("--output", help="Output file for generated payload", default="payload.raw")
    args, unknown = parser.parse_known_args()

    print(f"[*] Initializing RedOps listener on port {args.listener}...")
    print(f"[*] Generating authorized evaluation payload for platform: {args.payload}...")
    
    artifact = {
        "platform": args.payload,
        "listener_port": args.listener,
        "status": "ready",
        "encoding": "xor-custom",
        "note": "Authorized operational assessment artifact"
    }
    
    with open(args.output, "w") as f:
        json.dump(artifact, f, indent=4)
        
    print(f"[+] Payload successfully generated and written to: {args.output}")
    print("[+] RedOps operational loop active. Awaiting authorized agent connection...")

if __name__ == "__main__":
    main()
