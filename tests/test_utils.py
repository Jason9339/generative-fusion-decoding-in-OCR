import unittest
from collections import namedtuple
import importlib.util
import os

spec = importlib.util.spec_from_file_location(
    "gfd.utils", os.path.join(os.path.dirname(__file__), "..", "gfd", "utils.py")
)
utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(utils)
combine_config = utils.combine_config


class TestCombineConfig(unittest.TestCase):
    def test_combine_prefers_second(self):
        Config1 = namedtuple('Config1', ['a', 'b'])
        config1 = Config1(a=1, b=2)
        Config2 = namedtuple('Config2', ['b', 'c'])
        config2 = Config2(b=3, c=4)

        combined = combine_config(config1, config2)

        self.assertEqual(combined.a, 1)
        self.assertEqual(combined.b, 3)
        self.assertEqual(combined.c, 4)

