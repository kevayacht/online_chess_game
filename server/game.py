"""The game class is intended to encapsulate all objects and data related to
an instance of a typical game."""
from enum import Enum


class Game:

    def __init__(self):
        self.move_history = None
        self.player_one = None  # white
        self.player_two = None  # black
        self.last_move_made = None
        self.status = None
        self.time = None    # white, black, start time, elapsed time ?


class Status(Enum):
    """ The current status of the game as an enum class."""
    ACTIVE = 1
    WHITE_WIN = 2
    BLACK_WIN = 3
    FORFEIT = 4
    STALEMATE = 5
    RESIGNATION = 6
    EXPIRED_TIME = 7


class MoveHistory:
    """ The class records and handles the move history and notation for the
    current game."""

    def __init__(self):
        self.state = None  # Status()
        self.board = None
        self.taken_white_pieces = None
        self.taken_black_pieces = None
        self.current_turn = None
        self.notation = None  # dictionary of 2 dictionaries numbered with
        # the notations.
