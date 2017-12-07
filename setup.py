import os


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

clearScreen()
showTitle()
setupPlayer()
