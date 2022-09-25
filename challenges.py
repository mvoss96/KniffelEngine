class Challenge:
    """Interface for Challenges"""

    def __init__(self) -> None:
        self.name = "Platzhalter"
        self.completed: bool = False
        self.points: int = 0
        self.values = []

    def __str__(self) -> str:
        return (
            f"Challenge:{self.name:<13} completed:{str(self.completed):<5}"
            f" points:{self.points:<2} maxPoints:{self.get_max_points():<2} values:{str(self.values):<15}"
        )

    def get_points(self) -> int:
        return self.points

    def calc_points(self, input: list[int]) -> int:
        raise NotImplementedError

    def get_max_points(self) -> int:
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

    def get_max_points(self) -> int:
        return self.number_to_collect * 5

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

    def get_max_points(self) -> int:
        return self.collect_n * 6

    def calc_points(self, input: list[int]) -> int:
        val: int = 0
        for i in range(1, 7):
            if input.count(i) >= self.collect_n and i > val:
                val = i
        return val * self.collect_n


class Ch_full_house(Challenge):
    """Challenge: Collect 3 of one number and 2 of another number"""

    def __init__(self) -> None:
        super().__init__()
        self.name = "Full House"

    def get_max_points(self) -> int:
        return 25

    def calc_points(self, input: list[int]) -> int:
        if input[0] != input[1] or input[3] != input[4]:
            return 0
        if input[2] != input[1] and input[2] != input[3]:
            return 0
        return self.get_max_points()


class Ch_small_street(Challenge):
    """Challenge: Collect 4 consecutive numbers"""

    accepted_inputs = (set([1, 2, 3, 4]), set([2, 3, 4, 5]), set([3, 4, 5, 6]))

    def __init__(self) -> None:
        super().__init__()
        self.name = "Kleine Straße"

    def get_max_points(self) -> int:
        return 30

    def calc_points(self, input: list[int]) -> int:
        for tst in self.accepted_inputs:
            if tst <= set(input):  # if list is sublist of input
                return self.get_max_points()
        return 0


class Ch_big_street(Challenge):
    """Challenge: Collect 5 consecutive numbers"""

    accepted_inputs = ([1, 2, 3, 4, 5], [2, 3, 4, 5])

    def __init__(self) -> None:
        super().__init__()
        self.name = "Große Straße"

    def get_max_points(self) -> int:
        return 40

    def calc_points(self, input: list[int]) -> int:
        if input in self.accepted_inputs:
            return self.get_max_points()
        else:
            return 0
