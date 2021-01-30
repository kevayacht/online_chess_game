from enum import Enum

class Status(Enum):
    """ The current status of the game as an enum class."""
    ACTIVE = 1
    WHITE_WIN = 2
    BLACK_WIN = 3
    FORFEIT = 4
    STALEMATE = 5
    RESIGNATION = 6
    EXPIRED_TIME = 7
