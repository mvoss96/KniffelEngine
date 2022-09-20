class Challenge:
    """Interface for Challenges"""

    def __init__(self) -> None:
        self.name = "Platzhalter"
        self.completed: bool = False
        self.points: int = 0
        self.values = []

    def __str__(self) -> str:
        return f"Challenge:{self.name} completed:{self.completed} points:{self.points} values:{self.values}"

    def get_points(self) -> int:
        return self.points

    def calc_points(self, input: list[int]) -> int:
        raise NotImplementedError

    def set_result(self, input: list[int]) -> int:
        input.sort()
        self.points = 0
        self.completed = True
        self.points = self.calc_points(input)
        self.values = input
        return self.points

    def get_name(self) -> str:
        return self.name


class Ch_only_number(Challenge):
    """Challenge: Collect a specific number"""

    NAMESLIST: list[str] = ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"]

    def __init__(self, number_to_collect: int) -> None:
        super().__init__()
        if number_to_collect < 0 or number_to_collect > 6:
            raise ValueError("this challenge must only have values between 1 - 6")
        self.name = self.NAMESLIST[number_to_collect - 1]
        self.number_to_collect = number_to_collect

    def calc_points(self, input: list[int]) -> int:
        tmp: int = 0
        for i in input:
            if i == self.number_to_collect:
                tmp += i
        return tmp


class Ch_n_of_a_kind(Challenge):
    """Challenge: Collect n of the same number"""

    NAMESLIST: list[str] = [
        "--",
        "Zweierpasch",
        "Dreierpasch",
        "Viererpasch",
        "Kniffel",
    ]

    def __init__(self, collect_n: int) -> None:
        super().__init__()
        self.name = self.NAMESLIST[collect_n - 1]
        if collect_n < 0 or collect_n > 5:
            raise ValueError("this challenge must only have values between 1 - 5")
        self.collect_n = collect_n

    def calc_points(self, input: list[int]) -> int:
        val: int = 0
        for i in range(1, 7):
            if input.count(i) >= self.collect_n and i > val:
                val = i

        return val * self.collect_n