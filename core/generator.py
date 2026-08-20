import json
import os

class ActiveExploitEngine:
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

    def get_exploit_by_cve(self, cve_id):
        match = next((v for v in self.payload_db if v['cve'].upper() == cve_id.upper()), None)
        if not match:
            return None
        
        # Customize exploit code with user's LHOST and LPORT
        code = match['exploit_code'].replace('LHOST', self.lhost).replace('LPORT', str(self.lport))
        match['custom_exploit'] = code
        return match
