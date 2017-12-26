from character import *
from items import *

class Enemy(Character):

    def __init__(self, _name, _rage_points, _society_points):
        """
            Initializes an Enemy object.
            Attributes:
                Every attribute of Character
        """
        Character.__init__(self)
        self.set_name(_name)
        self.set_rage_points(_rage_points)
        self.set_society_points(_society_points)
        self.ability = ''
    #
    # Implementing Getters.
    #    
    def get_ability(self):
        """Method for safely get the special ability of Enemies"""
        return self.ability
    
    def set_ability(self, _ability_desc):
        """Methof for setting the special ability of enemies"""
        self.ability = _ability_desc
    


ENEMY_ABILITIES = {
    # TODO, maybe a dictionary for special enemy abilities like the Player's weapons but not sure yet.
}

