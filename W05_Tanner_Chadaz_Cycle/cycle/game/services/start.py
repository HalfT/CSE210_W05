from game.casting.cycle import Cycle
from game.casting.score import Score

class Start():
    """
    Helps start the game with two players, cycles, and scores

    The responsability of Start is to start the first game and also reset the cycles when the game
    is being replayed

    Attributes:
        _first_time (bool): teturns true for the first time played
    """

    def __init__(self):
        """Constructs a new instance of Start"""
        self._first_time = True
        
    def replay(self, cast):
        """Clears all cast members, then creates new ones ready for a new game.
        
        Args:
            cast (Cast): The cast of actors in the game."""
        cast.clear_cast()
        cycle1 = Cycle("player1")
        cycle2 = Cycle("player2")
        cast.add_actor("cycles", cycle1)
        cast.add_actor("cycles", cycle2)
        score1 = Score("player1")
        score2 = Score("player2")
        cast.add_actor("scores", score1)
        cast.add_actor("scores", score2)