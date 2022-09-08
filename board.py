
class Board(object):

    def __init__(self, width: int, heigth: int):
        self.width = width
        self.heigth = heigth
        self._board = None

    @property
    def board(self):
        if not self._board:
            self._board = [[True for column in range(
                self.heigth)] for row in range(self.width)]
        return self._board

    def draw_block(self, x: int, y: int):
        if x < 0 or y < 0:
            raise IndexError(f"Combination of x,y:{x},{y} out of range.")
        self.board[x][y] = False

    def get_cell(self, x: int, y: int):
        if x < 0 or y < 0:
            raise IndexError(f"Combination of x,y:{x},{y} out of range.")
        return self.board[x][y]

    def is_cell_available(self, x: int, y: int):
        return 0 <= x < self.width and 0 <= y < self.heigth and self.board[x][y]

    def copy(self):
        return Board(self.width, self.heigth)
