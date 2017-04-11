from context import wau
from wau import *

import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_import(self):
        assert(cu.green('green') == '\033[0;32mgreen\033[0;00m')


if __name__ == '__main__':
    unittest.main()
