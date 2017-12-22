import os

#
# Implementing functions for clear the terminal, and showing the Title.
#
def clearScreen():
    """
    Simple function that clears the screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def showTitle():
    """
    Just printing the title: "Stick It to the MAN" on cmd.
    """
    print("----------------------------------------------------------------------------------------")
    print("  _____ _   _      _      _____ _     _          _   _            __  __          _   _ ")
    print(" / ____| | (_)    | |    |_   _| |   | |        | | | |          |  \/  |   /\   | \ | |")
    print("| (___ | |_ _  ___| | __   | | | |_  | |_ ___   | |_| |__   ___  | \  / |  /  \  |  \| |")
    print(" \___ \| __| |/ __| |/ /   | | | __| | __/ _ \  | __| '_ \ / _ \ | |\/| | / /\ \ | . ` |")
    print(" ____) | |_| | (__|   <   _| |_| |_  | || (_) | | |_| | | |  __/ | |  | |/ ____ \| |\  |")
    print("|_____/ \__|_|\___|_|\_\ |_____|\__|  \__\___/   \__|_| |_|\___| |_|  |_/_/    \_\_| \_|")
    print("----------------------------------------------------------------------------------------")
    print("                                                                              by GTzakis")

#
# Clear terminal and starting the game.
clearScreen()
showTitle()

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
                self.rage (int, rage points)
                self.society (int, society points)
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
    
    def set_rage_points(self, _rage_points):
        """Method for safely setting Rage Points"""
        self.rage_points = _rage_points
    
    def set_society_points(self, _society_points):
        """Method for safely setting Society(xp) Points"""
        self.society_points = _society_points


#
# Implementing Player class, for the User's Player
#
class Player(Character):
    """User's player class, inherits from Character class."""

    def __init__(self, _username):
        """
            Initializes a Player object.
            Attributes:
                every attribute from Character-class objects.
                setting name with the User's PlayerName.
        """
        Character.__init__(self)
        self.set_name(_username)
        


#
# This code will be deleted.
#
user = Player("MakisDaDog!")
print(user.get_name(), user.get_health(), user.get_rage_points(), user.get_society_points())
