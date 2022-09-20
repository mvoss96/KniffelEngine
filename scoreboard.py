import copy
from challenges import *

def check_list_valid(input: list[int]):
    if len(input) != 5:
            raise ValueError("input must have length 5")
    for i in input:
        if i < 1 or i > 6:
            raise ValueError("input must only have values between 1 - 6")



class Scoreboard:
    """Holds all data for one player"""

    def __init__(self) -> None:
        points_for_upper_bonus: int = 63
        self.upper_challenges: list[Challenge] = [
            Ch_only_number(i) for i in range(1, 7)
        ]
        self.lower_challenges: list[Challenge] = [
            Ch_n_of_a_kind(3),
            Ch_n_of_a_kind(4),
            Ch_n_of_a_kind(5),
        ]

    def get_upper(self) -> list[Challenge]:
        return copy.deepcopy(self.upper_challenges)

    def get_lower(self)-> list[Challenge]:
        return copy.deepcopy(self.lower_challenges)

    def apply_upper(self, input: list[int], ch: int) -> int:
        check_list_valid(input)
        return self.upper_challenges[ch].set_result(input)

    def apply_lower(self, input: list[int], ch: int) -> int:
        check_list_valid(input)
        return self.lower_challenges[ch].set_result(input)

    def get_points(self) -> int:
        points: int = 0
        for ch in self.upper_challenges:
            if ch.completed:
                points += ch.get_points()
        return points
