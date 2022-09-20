import random


class Dice:
    """Contains methods to roll dices"""

    def __init__(self) -> None:
        # set random seed to system time
        random.seed()

    def roll(self, num_of_dice: int = 1) -> list[int]:
        """Roll dices
        Args:
            num_of_dice (int, optional): Number of dices to roll. Defaults to 1.
        Returns:
            list[int]: Rolled values
        """
        out = []
        sides = 6
        for i in range(num_of_dice):
            # random int from 1 -> sides (inclusive)
            random_number: int = random.randint(1, sides)
            out.append(random_number)
        out.sort()
        return out
