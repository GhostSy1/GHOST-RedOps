import json


class ShellGenerator:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def _not_generated(self, family):
        return json.dumps({
            'family': family,
            'status': 'not_generated',
            'reason': 'Executable remote-command payload generation is not included in the public build.',
            'requested_listener': {'address': self.ip, 'port': self.port}
        }, sort_keys=True)

    def python_shell(self):
        return self._not_generated('python')

    def bash_shell(self):
        return self._not_generated('bash')

    def powershell_shell(self):
        return self._not_generated('powershell')

    def php_shell(self):
        return self._not_generated('php')
