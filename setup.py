#
# Setup file for the main game functionality.
#
import os

from character import *
from items import *
from enemies import *
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

# user_name = input("Who do you think you are punk!?\n")

# user_player = Player(user_name)
# user_player.printStats()

#
# TODO, decide how the fights will take place. And how the whole game-story will be.
# TODO, do i need getters, setters. I know is not the pythonic way, but maybe to keep them for now!?

#
# This code will be deleted.
#
user = Player("MakisDaDog!")
print(user.get_name(), user.get_health(), user.get_rage_points(), user.get_society_points())
test = Enemy("cop", 50, 30)
print("you have :", user.get_health(), "of hp.")
print("Your enemy is a crazy cop and ", test.get_ability())
test.printStats()
print(user.get_health())

user.set_health(user.get_health() - test.get_rage_points())
print(user.health)