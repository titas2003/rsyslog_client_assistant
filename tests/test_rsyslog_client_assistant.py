import unittest
from rsyslog_client_assistant.rsyslog_client_assistant import client_ruleset_config, apply_ruleset_client

class TestClientConfig(unittest.TestCase):
    def test_client_ruleset_config(self):
        result = client_ruleset_config('testRule', '127.0.0.1', 514, 'tcp')
        self.assertIn('ruleset(name="testRule")', result)

    def test_apply_ruleset_client(self):
        result = apply_ruleset_client('/var/log/test.log', 'testTag', 'local3', 'info', 'testRule')
        self.assertIn('input(type="imfile"', result)

if __name__ == '__main__':
    unittest.main()
