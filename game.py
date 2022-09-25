from dice import Dice
from scoreboard import Scoreboard

dice = Dice()
board = Scoreboard()

roll = dice.roll(5)
print(roll)
print(board.apply_lower([2,4,3,4,5], 3))
for i in board.get_lower(): print(i)
