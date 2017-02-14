import unittest

from n_queen2 import NQueen


class Test(unittest.TestCase):

    def test4(self):
        queen = NQueen(4)
        queen.search()

        if queen._board is not None:
            queen._board.print()

    def test5(self):
        queen = NQueen(5)
        queen.search()

        if queen._board is not None:
            queen._board.print()

    def test6(self):
        queen = NQueen(6)
        queen.search()

        if queen._board is not None:
            queen._board.print()

    def test7(self):
        queen = NQueen(7)
        queen.search()

        if queen._board is not None:
            queen._board.print()

    def test8(self):
        queen = NQueen(8)
        queen.search()

        if queen._board is not None:
            queen._board.print()


if __name__ == '__main__':
    unittest.main()