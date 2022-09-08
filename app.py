import unittest
from game import numberOfPaths


class TestGame(unittest.TestCase):

    def test1(self):
        n = 1
        board = [4, 3]
        snake = [[2, 2],  [3, 2],  [3, 1],  [3, 0],  [2, 0],  [1, 0],  [0, 0]]
        depth = 3
        result = 7

        paths = numberOfPaths(board, snake, depth)
        self.assertEqual(
            result, paths, f"Result should be {result} instead of {paths}")
        print_results(n, board, snake, depth, paths)

    def test2(self):
        n = 2
        board = [2, 3]
        snake = [[0, 2],  [0, 1],  [0, 0],  [1, 0],  [1, 1],  [1, 2]]
        depth = 10
        result = 1

        paths = numberOfPaths(board, snake, depth)
        self.assertEqual(
            result, paths, f"Result should be {result} instead of {paths}")
        print_results(n, board, snake, depth, paths)

    def test3(self):
        n = 3
        board = [10, 10]
        snake = [[5, 5],  [5, 4],  [4, 4],  [4, 5]]
        depth = 4
        result = 81

        paths = numberOfPaths(board, snake, depth)
        self.assertEqual(
            result, paths, f"Result should be {result} instead of {paths}")
        print_results(n, board, snake, depth, paths)


def print_results(n, board, snake, depth, paths):
    print((f"Test {n}: \n\t- board: \"{board}\"\n\t- snake: \"{snake}\""
           f"\n\t- depth: \"{depth}\" \nTotal paths: \"{paths}\"\n\n"))


if __name__ == "__main__":
    unittest.main()
