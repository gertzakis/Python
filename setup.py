import os

#
# Implementing functions for clear the terminal, and showing the Title.
#
def clearScreen():  
    """
    Simple function that clears the screen
    """
    os.system('cls' if os.name=='nt' else 'clear')

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

# Clear terminal and starting the game.
clearScreen()
showTitle()

#
# Implementing Class for basic characters.
#
class Character(object):
    """Basic class for characters in the game, including the player"""

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
        self.rage = 0
        self.society = 0
    #
    # Implementing Getters.
    #
    def get_name(self):
        """Method for safely access the name"""
        return self.name
    
    def get_health(self):
        """Method for safely get the health points"""
        return self.health

    def get_rage(self):
        """Method for safely get rage points""" 
        return self.rage

    def get_society(self):
        """Method for getting society points"""
        return self.society


#
# This code will be deleted.
#
def setupPlayer():
    """
    Setting up Player.
    Asking name of the player.
    Setting up Health/Mana points(100/100).
    """
    # global name, Health Points, Mana Points, Rebel Points
    global player_name
    global player_health_points 
    global player_mana_points
    global player_rebel_points
    # Our variable "name" is used to store our name, captured by keyboard input.
    player_name = input("Who the hell do you think you are? \n")
    # randint is a great way of adding some variety to your players statistics.        
    player_health_points = 100
    player_mana_points = 100


user = Character()
print(user.get_name(), user.get_health(), user.get_rage(), user.get_society())
