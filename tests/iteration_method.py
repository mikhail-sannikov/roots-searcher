import unittest

from methods.iteration_method import get_root


class TestGetRoot(unittest.TestCase):
    def test_range_with_root(self):
        result = get_root(-1, 1, 1e-6)

        self.assertIsInstance(result['root'], float)
