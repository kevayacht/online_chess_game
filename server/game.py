"""The game class is intended to encapsulate all objects and data related to
an instance of a typical game."""


class Game:

    def __init__(self):
        self.move_history = None
        self.player_one = None  # white
        self.player_two = None  # black
        self.last_move_made = None
        self.status = None
        self.time = None  # white, black, start time, elapsed time ?
