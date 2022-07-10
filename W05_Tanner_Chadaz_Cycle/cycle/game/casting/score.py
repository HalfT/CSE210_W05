import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Score(Actor):
    """
    stores points
    
    The responsibility of Score is to display how many points each player has.

    Attributes:
        _player (string): Represents either player 1 or player 2
    """
    def __init__(self, player):
        super().__init__()
        self._player = player
        self.show_points()
        if self._player == "player2":
            self.set_position(Point(constants.MAX_X - 100, 0))

    def show_points(self):
        """displays scores"""
        if self._player == "player1":
            self.set_text(f"Score: {constants.PLAYER1_SCORE}")
        if self._player == "player2":
            self.set_text(f"Score: {constants.PLAYER2_SCORE}")