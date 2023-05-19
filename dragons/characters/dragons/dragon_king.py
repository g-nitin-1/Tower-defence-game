from .dragon import Dragon
from utils import terminators_win
from .scuba_thrower import ScubaThrower
from ..fighter import Fighter

class DragonKing(ScubaThrower):
    # END 4.3
    """The King of the colony. The game is over if a terminator enters his place."""

    name = 'King'
    # Begin 4.3
    # OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 7
    instantiated = False
    implemented = True

    # END 4.3

    def __init__(self, armor=1):
        # BEGIN 4.3
        Dragon.__init__(self, armor)
        self.isDragonKing = False

        # Check if DragonKing is already instantiated or not
        if DragonKing.instantiated == False:
            self.isDragonKing = True
            DragonKing.instantiated = True

        # END 4.3

    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.
        Impostor kings do only one thing: reduce their own armor to 0.
        """
        # BEGIN 4.3
        if not self.isDragonKing:
            self.reduce_armor(self.armor)
        else:
            super().action(colony)
            current_pos = self.place
            current_pos = current_pos.exit
            while current_pos is not None:
                if current_pos.dragon is not None:
                    if not current_pos.dragon.is_buffed:
                        current_pos.dragon.damage *= 2
                        current_pos.dragon.is_buffed = True
                    if current_pos.dragon.is_container and current_pos.dragon.contained_dragon is not None and not current_pos.dragon.contained_dragon.is_buffed:
                        current_pos.dragon.contained_dragon.damage *= 2
                        current_pos.dragon.contained_dragon.is_buffed = True
                current_pos = current_pos.exit
        # END 4.3

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game.
        """
        # BEGIN 4.3
        Fighter.reduce_armor(self, amount)
        if self.armor <= 0 and self.isDragonKing:
            terminators_win()