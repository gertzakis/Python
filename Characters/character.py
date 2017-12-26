from items import *
#
# Implementing basic Class for Characters.
#
class Character(object):
    """Basic class for all the Characters in the game."""

    def __init__(self):
        """
            Initializes a Character object.
            Attributes:
                self.name (string, name of the character)
                self.health (int, health points)
                self.rage_points (int, rage points)
                self.society_points (int, society points)
        """
        self.name = ''
        self.health = 100
        self.rage_points = 0
        self.society_points = 0
    #
    # Implementing Getters.
    #
    def get_name(self):
        """Method for safely access the name"""
        return self.name

    def get_health(self):
        """Method for safely get the health points"""
        return self.health

    def get_rage_points(self):
        """Method for safely get rage points"""
        return self.rage_points

    def get_society_points(self):
        """Method for getting society points"""
        return self.society_points    
    #
    # Implementing needed setters.
    #
    def set_name(self, _character_name):
        """Method for safely setting character name"""
        self.name = _character_name
    
    def set_health(self, _health):
        """Method for safely changing character's health points after getting hit."""
        self.health = _health
    
    def set_rage_points(self, _rage_points):
        """Method for safely setting Rage Points"""
        self.rage_points = _rage_points
    
    def set_society_points(self, _society_points):
        """Method for safely setting Society(xp) Points"""
        self.society_points = _society_points

    def printStats(self):
        """Method for printing all the basic stats for the Characters"""
        print("\n")
        print(self.name,"'s stats:")
        print("Health Points:   ", self.health)
        print("Rage points:     ", self.rage_points)
        print("Society points:  ", self.society_points)
        print("\n")



