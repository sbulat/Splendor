# -*- coding: utf-8 -*-

from Tkinter import *
from Globals import Glob
from Game import *
from Card import *
from Token import *


### glowny program

Glob.root.resizable(0,0)
Glob.root.title("Splendor")
Glob.canvas.pack()
Glob.canvas.bind("<Button-1>", Glob.B1_click)
# Glob.canvas.bind("<Key>", Glob.key_pressed)

for i in range(40):
	FirstLevelCard(40,350)

Glob.canvas.create_rectangle(40, 350, 40+Glob.SIZE_X, 350+Glob.SIZE_Y, fill='black')

for i in range(30):
	SecondLevelCard(40,200)

Glob.canvas.create_rectangle(40, 200, 40+Glob.SIZE_X, 200+Glob.SIZE_Y, fill='black')

for i in range(20):
	ThirdLevelCard(40,50)

Glob.canvas.create_rectangle(40, 50, 40+Glob.SIZE_X, 50+Glob.SIZE_Y, fill='black')

# TODO: te trzy prostkaty ^ to karty majace zakrywać stosy. trzeba zrobić grafiki i wstawić

tmpStones = Glob.stonesNames*5
for stone in tmpStones:
	Glob.tokensPos[stone][1]+=10
	Token(Glob.tokensPos[stone][0], Glob.tokensPos[stone][1], stone)
for pos in Glob.tokensPos:
	Glob.tokensPos[pos][1] -= 10


Glob.game = Game()
Glob.game.deal_cards()

Glob.root.mainloop()
