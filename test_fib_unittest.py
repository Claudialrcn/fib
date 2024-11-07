from fib import fibonacci_iterative
import unittest


class Test(unittest.TestCase):

    def test_fib_9_is_34(self):
        self.assertEqual(fibonacci_iterative(9), 34)

    def test_fib_negative_raise_error(self):
        with self.raises(ValueError):
            fibonacci_iterative(-1)


if __name__ == '__main__':
    unittest.main()
