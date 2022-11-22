import unittest

from scoreboard import Gameboard


class TestGameboard(unittest.TestCase):
    def __init__(self):
        self.gameboard = Gameboard()

    def has_needed_attributes(self):
        height = self.gameboard.window_height()
        width = self.gameboard.window_width()

        self.assertEqual(height, 600)
        self.assertEqual(width, 600)


if __name__ == '__main__':
    unittest.main()
