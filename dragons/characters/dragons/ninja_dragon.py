from .dragon import Dragon


class NinjaDragon(Dragon):
    """NinjaDragon does not block the path and damages all terminators in its place."""

    name = 'Ninja'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.4
    implemented = True
    blocks_path=False
    food_cost=5
    def __init__(self, armor=1):
        """Create a Dragon with a ARMOR quantity."""
        Dragon.__init__(self, armor)

    # END 2.4

    def action(self, colony):
        # BEGIN 2.4
        terminator_list_copy= [i for i in self.place.terminators]
        for i in terminator_list_copy:
            i.reduce_armor(self.damage)
