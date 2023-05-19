from .thrower_dragon import ThrowerDragon


class LongThrower(ThrowerDragon):
    """A ThrowerDragon that only throws stones at Terminators at least 5 places away."""

    name = 'Long'
    food_cost=2
    min_range=5
    max_range=float('inf')
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.1
    implemented = True 
    def __init__(self, armor=1):
        """Create a Dragon with a ARMOR quantity."""
        ThrowerDragon.__init__(self, armor)
    # END 2.1
