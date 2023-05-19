from .container_dragon import ContainerDragon


class BodyguardDragon(ContainerDragon):
    """BodyguardDragon provides protection to other Dragons."""

    name = 'Bodyguard'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.2
    implemented = True
    food_cost=4

    def __init__(self, armor=2):
        ContainerDragon.__init__(self, armor)
        self.contained_dragon = None  # The Dragon hidden in this bodyguard

