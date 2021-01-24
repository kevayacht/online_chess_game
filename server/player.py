"""This object, the Player class, is intended encapsulate, store and manipulate
all player related information at the in game state per instance of the
class."""


class Player:

    def __init__(self):
        self.first_login = None
        self.last_active = None
        self.username = None
        self.uuid = None
        self.rank = None
        self.rating = None

    def get_player_data(self):
        pass
