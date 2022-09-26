import random
from xmlrpc.client import boolean
import challenges


class Kniffelgame:
    def __init__(self) -> None:
        random.seed()  # set random seed to system time
        self.players = []
        self.upper_challenges: list[challenges.Challenge] = [
            challenges.ch_only_number(i) for i in range(1, 7)  # Einser bis Sechser
        ]
        self.lower_challenges: list[challenges.Challenge] = [
            challenges.ch_n_of_a_kind(3),  # Dreierpasch
            challenges.ch_n_of_a_kind(4),  # Viererpasch
            challenges.ch_full_house(),  # Full House
            challenges.ch_small_street(),  # Kleine Straße
            challenges.ch_big_street(),  # Große Straße
            challenges.ch_n_of_a_kind(5),  # Kniffe
        ]

    def roll(self, num_of_dice: int = 1) -> list[int]:
        """Roll dices
        Args:
            num_of_dice (int, optional): Number of dices to roll. Defaults to 1.
        Returns:
            list[int]: Rolled values
        """
        out = []
        for _ in range(num_of_dice):
            random_number: int = random.randint(1, 6)
            out.append(random_number)
        out.sort()
        return out

    def get_empty_challenge_entry(self, ch: challenges.Challenge) -> dict:
        ch_entry = {}
        ch_entry["name"] = ch.get_name()
        ch_entry["points"] = None
        ch_entry["max_points"] = ch.get_max_points()
        ch_entry["dice"] = None
        return ch_entry

    def get_empty_scoreboard(self) -> dict:
        scoreboard: dict = {
            "player": "",
            "dice": [],
            "dice_marked": False,
            "rolls": 0,
            "completed": False,
            "upper_challenges": [],
            "lower_challenges": [],
            "upper_score": 0,
            "bonus": 0,
            "lower_score": 0,
        }
        for ch in self.upper_challenges:
            scoreboard["upper_challenges"].append(self.get_empty_challenge_entry(ch))  # type: ignore
        for ch in self.lower_challenges:
            scoreboard["lower_challenges"].append(self.get_empty_challenge_entry(ch))  # type: ignore
        return scoreboard

    def add_player(self, playername: str) -> int:
        board = self.get_empty_scoreboard()
        board["player"] = playername
        self.players.append(board)
        return len(self.players)

    def player_roll_dice(self, player_number: int) -> tuple:
        if player_number < 1 or player_number > len(self.players):
            print("ERROR: Player does not exist!")
            return ([], [])
        player: dict = self.players[player_number - 1]
        if player["rolls"] > 2:
            print("ERROR: All rolls were already used!")
            return ([], [])
        rolled_dice: list[int] = self.roll(5 - len(player["dice"]))
        player["dice_marked"] = False
        player["dice"] += rolled_dice
        player["dice"].sort()
        player["rolls"] += 1
        return (player["dice"], rolled_dice)

    def player_mark_dice_to_reroll(
        self, player_number: int, dice_to_reroll: list[boolean]
    ) -> int:
        if len(dice_to_reroll) != 5:
            print("ERROR: dice list must have lenght 5")
            return -1
        player: dict = self.players[player_number - 1]
        if player["dice_marked"] == True:
            print("ERROR: dice already marked for reroll")
            return -2
        if player["rolls"] not in (1, 2):
            print("ERROR: dice can only be marked after roll 1 and 2")
            return -3
        player["dice_marked"] = True
        n_marked: int = 0
        for i, dice in enumerate(dice_to_reroll):
            if dice:
                n_marked += 1
                player["dice"].pop(i)
        return n_marked


if __name__ == "__main__":
    game = Kniffelgame()
    p = game.add_player("testplayer")
    print(game.player_roll_dice(p))
    game.player_mark_dice_to_reroll(p, [True, False, False, False, False])
    print(game.player_roll_dice(p))
    game.player_mark_dice_to_reroll(p, [False, False, False, True, False])
    print(game.player_roll_dice(p))
