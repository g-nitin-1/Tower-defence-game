from .dragon import Dragon
from utils import random_or_none

class HungryDragon(Dragon):
    """HungryDragon will take three turns to digest a Terminator in its place.
    While digesting, the HungryDragon can't eat another Terminator.
    """
    name = 'Hungry'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.3
    time_to_digest=3
    food_cost=4
    implemented = True 

    # END 2.3

    def __init__(self, armor=1):
        # BEGIN 2.3
        Dragon.__init__(self,armor)
        self.digesting=0
        # END 2.3

    def eat_terminator(self, terminator):
        # BEGIN 2.3
        terminator.armor=0
        self.place.remove_fighter(terminator)
        terminator.death_callback()
        # END 2.3

    def action(self, colony):
        # BEGIN 2.3
        if(self.place!=None and self.place.name!='Skynet'):
            if(self.digesting):
                self.digesting-=1
            else:
                if(random_or_none(self.place.terminators)!=None):
                    self.eat_terminator(random_or_none(self.place.terminators))
                    self.digesting=self.time_to_digest
