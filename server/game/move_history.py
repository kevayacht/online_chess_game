

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