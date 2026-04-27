import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add current directory to path
sys.path.append(os.getcwd() + '/ssh-botnet')

from ssh_botnet import Client, botnet_command, add_client

class MockPxssh:
    def __init__(self):
        self.before = b"mock output"
    def login(self, host, user, password):
        if password == "fail":
            raise Exception("Login failed")
        return True
    def sendline(self, cmd):
        pass
    def prompt(self):
        return True

class TestBotnet(unittest.TestCase):
    @patch('pexpect.pxssh.pxssh', side_effect=MockPxssh)
    def test_connection_success(self, mock_px):
        client = Client('127.0.0.1', 'user', 'pass')
        self.assertIsNotNone(client.session)
        
    @patch('pexpect.pxssh.pxssh', side_effect=MockPxssh)
    def test_command_execution(self, mock_px):
        client = Client('127.0.0.1', 'user', 'pass')
        output = client.send_command('ls')
        self.assertEqual(output, b"mock output")

    @patch('pexpect.pxssh.pxssh', side_effect=MockPxssh)
    def test_botnet_command_success(self, mock_px):
        botnet = []
        add_client(botnet, '127.0.0.1', 'user', 'pass')
        with patch('builtins.print') as mock_print:
            botnet_command(botnet, 'ls')
            # Check if output was printed
            mock_print.assert_any_call('[*] Output from 127.0.0.1')

if __name__ == '__main__':
    unittest.main()
