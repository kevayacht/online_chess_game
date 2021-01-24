"""The pawn class will describe the basic attributes and methods surrounding
the pawn piece in the game."""

from server.piece import Piece


class Pawn(Piece):

    def __init__(self):
        super().__init__()
