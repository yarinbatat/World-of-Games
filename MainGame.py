from Live import *
from GuessGame import *
from MemoryGame import *
from CurrncyRouletteGame import *
from Score import *

(welcome(""))

use_game, use_level = load_game()

if use_game == 1:
    play1(use_level)
elif use_game == 2:
    play2(use_level)
elif use_game == 3:
    play3(use_level)
