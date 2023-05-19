from .dragon import Dragon
from utils import random_or_none

class ThrowerDragon(Dragon):
    """ThrowerDragon throws a stone each turn at the nearest Terminator in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    food_cost=3
    min_range=0
    max_range=float('inf')
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE

    def nearest_terminator(self, skynet):
        """Return the nearest Terminator in a Place that is not the SKYNET, connected to
        the ThrowerDragon's Place by following entrances.

        This method returns None if there is no such Terminator (or none in range).
        """
        # BEGIN 1.3 and 2.1
        temp=self.place
        for i in range(self.min_range):
            temp=temp.entrance
        if(random_or_none(temp.terminators)!=None and temp.name!='Skynet'):
            return random_or_none(temp.terminators)
        i=self.min_range
        while(temp.entrance!=None and temp.entrance.name!='Skynet' and i<self.max_range):
            i=i+1
            temp=temp.entrance
            if(random_or_none(temp.terminators)!=None):
                return random_or_none(temp.terminators)
        return None        
        # END 1.3 and 2.1

    def throw_at(self, target):
        """Throw a stone at the TARGET Terminator, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)

    def action(self, colony):
        """Throw a stone at the nearest Terminator in range."""
        self.throw_at(self.nearest_terminator(colony.skynet))
