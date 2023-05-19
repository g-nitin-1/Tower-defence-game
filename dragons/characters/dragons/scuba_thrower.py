from .thrower_dragon import ThrowerDragon
class ScubaThrower(ThrowerDragon):
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    food_cost=6
    is_watersafe=True
    name='Scuba'
    implemented=True
    
    def __init__(self,armor=1):
        ThrowerDragon.__init__(self,armor)
