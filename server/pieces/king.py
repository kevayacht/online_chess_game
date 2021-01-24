"""The king class will describe the basic attributes and methods surrounding
the king piece in the game."""

from server.piece import Piece


class King(Piece):

    def __init__(self):
        super().__init__()
