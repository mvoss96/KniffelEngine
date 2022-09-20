from dice import Dice
from scoreboard import Scoreboard

dice = Dice()
board = Scoreboard()

roll = dice.roll(5)
print(roll)
print(board.apply_lower([1,2,1,2,2], 2))
for i in board.get_lower(): print(i)
