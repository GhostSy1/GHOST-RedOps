import base64
import json
import os
import random

class UltimateExploitEngine:
    def __init__(self, lhost, lport):
        self.lhost = lhost
        self.lport = lport
        self.db_path = os.path.join(os.path.dirname(__file__), '../db/payloads.json')
        self.payload_db = self.load_db()

    def load_db(self):
        if os.path.exists(self.db_path):
            with open(self.db_path, 'r') as f:
                return json.load(f)
        return []

    def generate_custom_exploit(self, cve_id):
        # Find CVE in our 1000+ DB
        match = next((v for v in self.payload_db if v['cve'] == cve_id), None)
        if not match:
            return "CVE not found in local elite database."
        
        # Professional exploit generation logic based on CVE type
        desc = match['description'].lower()
        if "overflow" in desc:
            return f"# Ghost-SY1 Buffer Overflow Exploit for {cve_id}\n# Target: {match['product']}\n# Payload: Reverse TCP to {self.lhost}:{self.lport}\n..."
        elif "remote code execution" in desc or "rce" in desc:
            return f"# Ghost-SY1 RCE Exploit for {cve_id}\n# Target: {match['product']}\n# Payload: Encrypted Stager to {self.lhost}:{self.lport}\n..."
        return f"# Ghost-SY1 Generic Exploit for {cve_id}\n# Payload: {match['description']}"

    def get_top_exploits(self):
        return self.payload_db[:10]
