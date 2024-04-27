# Test Cases: Paste in the Same Directory as the oxo_cmd file before running
import oxo_cmd
import unittest as ut
from unittest.mock import patch

class t3tester(ut.TestCase):
    @patch('builtins.input', side_effect=['new', '1', '5', '9', 'quit', 'y'])
    def test_primary(self, mock_input):
        with self.assertRaises(SystemExit):
            oxo_cmd.main()   

if __name__ == "__main__":
    ut.main()