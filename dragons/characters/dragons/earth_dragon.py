from .dragon import Dragon

class EarthDragon(Dragon):
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    name='Earth'
    implemented=True
    damage=0
    food_cost=4
    def __init__(self, armor=4):
        """Create a Dragon with a ARMOR quantity."""
        Dragon.__init__(self, armor)
