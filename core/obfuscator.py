import base64
import random
import string
class PayloadObfuscator:
    def __init__(self, raw_payload):
        self.payload = raw_payload
    def xor_cipher(self, data, key):
        return "".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))
    def generate_key(self, length=16):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    def b64_encode(self, data):
        return base64.b64encode(data.encode()).decode()
    def obfuscate(self):
        key = self.generate_key()
        xor_data = self.xor_cipher(self.payload, key)
        b64_xor = self.b64_encode(xor_data)
        return b64_xor, key
