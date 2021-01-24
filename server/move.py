"""The Move class will encapsulate all instances of changes applied to the
game instance throughout its duration. """


class Move:

    def __init__(self):
        self.starting_box = None
        self.ending_box = None
        self.piece_selected = None
        self.player_owner = None
        self.is_in_check = None

    def action(self):
        pass
