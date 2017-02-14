import copy


class Board(object):
    def __init__(self, N):
        self._n = N
        self._availability = [[True for ii in range(N)] for jj in range(N)]

        self._pos = []

    def add(self, pos):
        self._mark(pos)
        self._pos.append(pos)

    def _mark(self, pos):
        x, y = pos

        assert 0 <= x < self._n and 0 <= y < self._n

        for jj in range(self._n):
            self._availability[x][jj] = False

        for ii in range(self._n):
            self._availability[ii][y] = False

        self._mark_diagonals(pos)

    def _mark_diagonals(self, pos):
        for direc in (1, 1), (1, -1), (-1, 1), (-1, -1):
            self._mark_diagonal(pos, direc)

    def _mark_diagonal(self, pos, direction):
        ii, jj = direction
        x, y = pos

        while 0 <= x + ii < self._n and 0 <= y + jj < self._n:
            x += ii
            y += jj
            self._availability[x][y] = False

    def next(self):
        for ii in range(self._n):
            for jj in range(self._n):
                if self._availability[ii][jj]:
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
