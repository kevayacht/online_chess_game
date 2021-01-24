"""The queen class will describe the basic attributes and methods surrounding
the queen piece in the game."""

from server.piece import Piece


class Queen(Piece):

    def __init__(self):
        super().__init__()
