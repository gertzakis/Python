#
# File for the Player's class.
#
from Characters.character import *
from items import *
#
# Implementing Player class, for the User's Player
#
class Player(Character):
    """User's player class, inherits from Character class."""

    def __init__(self, _username):
        """
            Initializes a Player object.
            Attributes:
                Character.__init__ (every attribute of the Character class)
                self.set_name (setter of the Character class, changing the name 
                    of the object)
                self.weapon (items.object, the weapon the player uses at the time)
        """
        Character.__init__(self)
        self.set_name(_username)
        self.weapon = ITEMS['yell']
    #
    # Implementing Getters.
    #
    def get_weapon(self):
        """Method for safely getting the weapon of the Player."""
        return self.weapon
    #
    # Implementing Setters for the Player.
    #
    def set_weapon(self, _new_weapon):
        """
            Method for safely changing the using weapon of the Player.
            Input: _new_weapon (string, as key to the ITEMS dictionary)
        """
        self.weapon = ITEMS[_new_weapon]