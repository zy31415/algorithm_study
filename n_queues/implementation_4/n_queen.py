import copy


def print_board(board):
    N = len(board)
    for ii in range(N):
        for jj in range(N):
            if jj == board[ii]:
                print("*", end=' ')
            else:
                print('0', end=' ')
        print()


class NQueen(object):
    def __init__(self, N):
        self._n = N
        self._results = []

    def search(self, board=None, nrow=None):

        if board is None:
            board = [-1 for ii in range(self._n)]
            nrow = 0

        if nrow >= self._n:
            if board[-1] >= 0:
                self._results.append(board)
                return

        cols = set(list(range(self._n)))

        for ii in range(nrow):
            assert board[ii] >= 0
            col = board[ii]
            for _col in col, col - (nrow - ii), col + (nrow - ii):
                if _col in cols:
                    cols.remove(_col)

        # recursive:
        for col in cols:
            _board = copy.copy(board)
            _board[nrow] = col
            self.search(_board, nrow+1)