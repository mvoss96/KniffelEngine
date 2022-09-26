import copy
from challenges import (
    Challenge,
    ch_only_number,
    ch_n_of_a_kind,
    ch_full_house,
    ch_big_street,
    ch_small_street,
)


def check_list_valid(input: list[int]):
    if len(input) != 5:
        raise ValueError("input must have length 5")
    for i in input:
        if i < 1 or i > 6:
            raise ValueError("input must only have values between 1 - 6")


class Scoreboard:
    """Holds all game data for one player"""

    points_for_upper_bonus: int = 63

    def __init__(self) -> None:
        self.upper_challenges: list[Challenge] = [
            ch_only_number(i) for i in range(1, 7)
        ]
        self.lower_challenges: list[Challenge] = [
            ch_n_of_a_kind(3),
            ch_n_of_a_kind(4),
            ch_full_house(),
            ch_small_street(),
            ch_big_street(),
            ch_n_of_a_kind(5),
        ]


    def get_upper_challenges(self) -> list[Challenge]:
        return copy.deepcopy(self.upper_challenges)

    def get_lower(self) -> list[Challenge]:
        return copy.deepcopy(self.lower_challenges)

    def apply_upper(self, input: list[int], ch: int) -> int:
        check_list_valid(input)
        return self.upper_challenges[ch].set_result(input)

    def apply_lower(self, input: list[int], ch: int) -> int:
        check_list_valid(input)
        return self.lower_challenges[ch].set_result(input)

    def points_upper(self) -> int:
        points: int = 0
        for ch in self.upper_challenges:
            if ch.completed:
                points += ch.get_points()
        return points

    def points_lower(self) -> int:
        points: int = 0
        for ch in self.lower_challenges:
            if ch.completed:
                points += ch.get_points()
        return points

    def points_bonus(self) -> int:
        return 35 if self.points_upper() >= self.points_for_upper_bonus else 0

    def get_points(self) -> int:
        return self.points_upper() + self.points_lower() + self.points_bonus()

    def get_report(self) -> dict:
        report = {}
        points: int = 0
        for i, ch in enumerate(self.upper_challenges):
            chname: str = f"{i}: " + ch.get_name()
            report[chname] = {}
            p: int = ch.get_points()
            report[chname]["points"] = p
            points += p
        report["sum_upper"] = {"points": points}
        report["bonus"] = {"points": self.points_bonus()}
        report["sum_upper_after_bonus"] = {"points": self.points_bonus()}

        for i, ch in enumerate(self.upper_challenges):
            chname: str = f"challenge{i}: " + ch.get_name()
            report[chname] = {}
            report[chname]["points"] = ch.get_points()
        return report
