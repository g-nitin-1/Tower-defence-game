from .thrower_dragon import ThrowerDragon


class ShortThrower(ThrowerDragon):
    """A ThrowerDragon that only throws stones at Terminators at most 3 places away."""

    name = 'Short'
    food_cost=2
    max_range=3
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.1
    implemented = True 
    def __init__(self, armor=1):
        """Create a Dragon with a ARMOR quantity."""
        ThrowerDragon.__init__(self, armor)
    # END 2.1
