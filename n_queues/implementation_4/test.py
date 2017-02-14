import unittest

from n_queen import NQueen, print_board


class Test(unittest.TestCase):

    def test8(self):
        self._test(8)

    def test12(self):
        self._test(13)

    def test13(self):
        self._test(13)

    def test14(self):
        self._test(14)

    def _test(self, N):
        queen = NQueen(N)
        queen.search()

        print("Found: %d"%len(queen._results))
        #
        # for b in queen._results:
        #     print_board(b)
        #     print("==========")

if __name__ == '__main__':
    unittest.main()