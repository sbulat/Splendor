# -*- coding: utf-8 -*-

from Tkinter import *
from Globals import Glob
from Game import *
from Card import *
from Token import *

def B1_click(event):
		for card in Glob.game.__getitem__():
			if card.a[0]<=event.x<=card.b[0] and card.a[1]<=event.y<=card.b[1]:
				Glob.game.actualPlayer.buy_card(card)
				return

		for token in Glob.tokens:
			if token.a[0]<=event.x<=token.b[0] and token.a[1]<=event.y<=token.b[1]:
				Glob.game.actualPlayer.get_token(token)
				return


### glowny program
Glob.root.resizable(0,0)
Glob.root.title("Splendor")
Glob.canvas.pack()
Glob.canvas.bind("<Button-1>", B1_click)

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
