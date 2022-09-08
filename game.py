from board import Board
from snake import Snake


class Game(object):

    def __init__(self, board: list, snake: list):
        self.board = Board(*board)
        self.snake = Snake(snake)

    def move_snake(self, direction):
        self.snake.move_snake(direction, self.board)

    def movements(self):
        return self.snake.sonar(self.board)

    def copy(self):
        return Game([self.board.width, self.board.heigth], self.snake.snake)


def numberOfPaths(board, snake, depth):
    # create a game
    game = Game(board, snake)
    # call the number of movements function
    return available_paths(game, depth)


def available_paths(game: Game, depth):
    if depth == 1:
        return len(game.movements())
    if depth == 0:
        return 0
    total_paths = 0
    for move in game.movements():
        game_copy = game.copy()
        game_copy.move_snake(move)
        total_paths += available_paths(game_copy, depth - 1)
    return total_paths
