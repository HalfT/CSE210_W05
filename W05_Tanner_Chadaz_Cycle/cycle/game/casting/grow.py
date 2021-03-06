from game.scripting.action import Action

class Grow(Action):
    """
    An update action that modifies cycles over time.
    
    The responsability of Grow is to grow the length of the cycle's tail
    
    Attributes:
        _counter (int): An iterating, self-resetting value used as a timer.
        _is_game_over (bool): The state of the game, whether over or not."""

    def __init__(self):
        """Contructs a new Grow instance."""
        self._counter = 0
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the modify actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        update_actions = script.get_actions("update")
        handle_collisions_action = update_actions[1]
        self._is_game_over = handle_collisions_action.is_game_over()
        if not self._is_game_over:
            self._counter += 3

            if self._counter >= 20:
                self._counter = 0

                cycles = cast.get_actors("cycles")
                for cycle in cycles:
                    cycle.grow_trail(1)