#
# Implementing Items Class for the Items of the characters.
#
class Items(object):
    """ Items Class for the Items of the game
        Input:
            _name (string, name of the item)
            _desc (string, description of the item)
            _attack_points(int, attack points of the item)
    """

    def __init__(self, _name, _desc, _attack_points, _rage_cost_points):
        """
            Initializes a Item object.
            Attributes:
                self.name (string, name of the item)
                self.desc (string, description of the item)
                self.attack_points (int, attack points)
        """
        self.name = _name
        self.desc = _desc
        self.attack_points = _attack_points
        self.cost_points = _rage_cost_points
    #
    # Implementing Getters.
    #
    def get_name(self):
        """Method for safely access the item name."""
        return self.name

    def get_desc(self):
        """Methof for safely access the description of the name."""
        return self.desc

    def get_attack_points(self):
        """Methof for safely access the attack_points of the item."""
        return self.attack_points

    def printStats(self):
        """Method for printing weapon stats"""
        print("\n")
        print("Item '",self.name,"' statistics.")
        print(self.desc)
        print("Attack points:   ", self.attack_points)
        print("Rage cost:       ", self.cost_points)
        print("\n")
    
    #
    # Implementing Setters.
    #
    # def set_name(self, _item_name):
    #     """Method for safely setting item name."""
    #     self.name = _item_name
    
    # def set_desc(self, _item_desc):
    #     """Method for safely setting description of item."""
    #     self.desc = _item_desc
    
    # def set_attack_points(self, _item_attack_points):
    #     """Method for safely setting attack points of the item."""
    #     self.attack_points = _item_attack_points
    


ITEMS = {
    # TODO, import more weapons for the Player, and decide if thats the best way to do it.
    "yell"      : Items("Yell", "Scream to all the fuckers out there bruv!", 10, 0),
    "fists"     : Items("Fists", "Nothing that cannot be solved with a good punch!", 20, 10),
    "bottle"    : Items("Bottle", "Broken bottle after enjoying a lager!", 30, 20),
    "crowbar"   : Items("Crowbar", "Time to mess with some real fuckers!", 40, 30),
    "molotov"   : Items("Molotov", "Perfect for riots and football matches!", 50, 40)
}
