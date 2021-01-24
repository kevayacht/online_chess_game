"""The bishop class will describe the basic attributes and methods surrounding
the bishop piece in the game."""

from server.piece import Piece


class Bishop(Piece):

    def __init__(self):
        super().__init__()
