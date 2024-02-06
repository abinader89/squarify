import unittest
from SquareFormatter import SquareFormatter


class Test(unittest.TestCase):
    def test_square_len0(self):
        squares = SquareFormatter()

        squares.members = ["Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob",
                           "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob",
                           "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob",
                           "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob",
                           "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob",
                           "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice",
                           "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice",
                           "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice",
                           "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice",
                           "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice"]

        squares.list_to_csv()

        self.assertEqual(len(squares.members), 100)  # add assertion here

    def test_square_len1(self):
        squares = SquareFormatter()

        squares.members = ["Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob",
                           "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice", "Alice"]
        squares.list_to_csv()

        self.assertEqual(len(squares.members), 100)  # add assertion here


if __name__ == '__main__':
    unittest.main()
