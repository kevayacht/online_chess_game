"""This object is intended to encapsulate the base class for all pieces in the
game and will be instantiated as such. This implies that the class will for
the most part serve as an interface to the chess pieces to ensure all pieces
have the needed functionality.
"""


class Piece:

    def __init__(self):
        self.notation_tag = None
        self.colour = None
        self.value = None

    def movement(self):
        pass
