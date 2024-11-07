import pytest

from fib import fibonacci_iterative
import unittest


class Test(unittest.TestCase):

    def test_fib_9_is_34(self):
        assert fibonacci_iterative(9) == 34

    def test_fib_negative_raise_error(self):
        with pytest.raises(ValueError):
            fibonacci_iterative(-1)
