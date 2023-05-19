from .dragon import Dragon


class FireDragon(Dragon):
    """FireDragon cooks any Terminator in its Place when it expires."""

    name = 'Fire'
    damage = 3
    food_cost=5
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.2
    implemented = True

    # END 2.2

    def __init__(self, armor=3):
        """Create a Dragon with a ARMOR quantity."""
        Dragon.__init__(self, armor)

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and remove the FireDragon from its place if it
        has no armor remaining.

        Make sure to damage each terminator in the current place, and apply the bonus
        if the fire dragon dies.
        """
        # BEGIN 2.2
        self.armor-=amount
        terminator_list_copy= [i for i in self.place.terminators]
        if self.armor<=0:
            for i in terminator_list_copy:
                i.reduce_armor(amount+self.damage)
            self.place.remove_fighter(self)
            self.death_callback()
        else:
            for i in terminator_list_copy:
                i.reduce_armor(amount)
        
