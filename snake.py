
from board import Board


class Snake(object):

    # dictionary with available moves
    movements = {"R": [1, 0], "D": [0, 1], "L": [-1, 0], "U": [0, -1]}

    def __init__(self, snake: list):
        self.snake = snake

    def sonar(self, board: Board):
        new_board = self.available_cells(board)
        movements = self.possible_movements()
        sonar = []
        for m in movements:
            try:
                if new_board.get_cell(*m[1]):
                    sonar.append(m[0])
            except IndexError:
                pass
        return sonar

    def possible_movements(self):
        head = self.snake[0]
        return [(k, [head[0]+v[0], head[1] + v[1]])
                for k, v in Snake.movements.items()]

    def available_cells(self, board: Board):
        new_board = board.copy()
        for i in range(len(self.snake)-1):
            body = self.snake[i]
            new_board.draw_block(*body)
        return new_board

    def move_snake(self, direction: str, board: Board):
        if direction not in Snake.movements.keys():
            raise Exception(f"Movimiento \"{direction}\" incorrecto.")
        if direction not in self.sonar(board):
            raise Exception(f"\"{direction}\", esta ocupada la celda")
        head = self.snake[0]
        move = Snake.movements[direction]
        self.snake = [[head[0] + move[0], head[1] + move[1]]] + self.snake[:-1]
