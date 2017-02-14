import copy


class Board(object):
    def __init__(self, N):
        self._n = N

        self._rows = [True for ii in range(N)]
        self._cols = [True for ii in range(N)]
        self._ldiag = [True for ii in range(2 * N - 1)] # \
        self._rdiag = [True for ii in range(2 * N - 1)] # /

        self._pos = []

    def add(self, pos):
        self._mark(pos)
        self._pos.append(pos)

    def _mark(self, pos):
        x, y = pos

        assert 0 <= x < self._n and 0 <= y < self._n

        self._rows[x] = False
        self._cols[y] = False
        self._ldiag[x-y] = False
        self._rdiag[x+y] = False

    def next(self):
        for ii in range(self._n):
            if self._rows[ii]:
                for jj in range(self._n):
                    if self._cols[jj]:
                        if self._ldiag[ii-jj] and self._rdiag[ii+jj]:
                            yield (ii, jj)

    def copy(self):
        return copy.deepcopy(self)

    def num_queues(self):
        return len(self._pos)

    def print(self):

        _pos = set(self._pos)

        for ii in range(self._n):
            for jj in range(self._n):
                if (ii, jj) in _pos:
                    print("*", end=' ')
                else:
                    print('0', end=' ')
            print()


class NQueen(object):
    def __init__(self, N):
        self._n = N
        self._board = None

    def search(self, board=None):

        if board is None:
            board = Board(self._n)

        if board.num_queues() == self._n:
            self._board = board
            return

        for pos in board.next():
            _board = board.copy()
            _board.add(pos)
            self.search(_board)
