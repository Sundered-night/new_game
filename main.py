from .actual_game.randomizer import ran
from .actual_game.input import input
from .actual_game.win_cond import vic
from random import randint

game = ["rock",'paper','scissor']
player  = False
count = 0

while count <= 5:
    ran()
    input()
    vic(player)
    player = False
    comp = game[randint(0,2)]
    count = count + 1    