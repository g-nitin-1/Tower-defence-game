from .bodyguard_dragon import BodyguardDragon


class TankDragon(BodyguardDragon):
    """TankDragon provides both offensive and defensive capabilities."""

    name = 'Tank'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.3
    implemented = True
    food_cost=6
    is_container=True

    # END 3.3

    def action(self, colony):
        # BEGIN 3.3
        BodyguardDragon.action(self,colony)
        terminator_list_copy= [i for i in self.place.terminators]
        for i in terminator_list_copy:
            i.reduce_armor(self.damage)

