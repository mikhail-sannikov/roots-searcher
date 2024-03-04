import unittest

from methods.bisection_method import get_root


class TestGetRoot(unittest.TestCase):
    def test_range_with_root(self):
        result = get_root(1, 3, 1e-6)

        self.assertIsInstance(result['root'], float)

    def test_range_without_root(self):
        root = get_root(9, 10, 1e-6)

        self.assertIsNone(root)
