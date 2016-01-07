# -*- coding: utf-8 -*-

from Tkinter import *
from Globals import Glob
from Game import *
from Card import *
from Token import *



# canvas.create_text(event.x, event.y, text="clicked at " + str(event.x) + ", " + str(event.y))
# def call(event):
# 	toPrint = "clicked at " + str(event.x) + ", " + str(event.y)
# 	canvas.create_text(event.x, event.y, text=toPrint)
# 	canvas.create_rectangle(0,0,20,20)


def doubleB1(event):
	for card in Glob.game.__getitem__():
		if card.a[0]<=event.x<=card.b[0] and card.a[1]<=event.y<=card.b[1]:
			Glob.game.actualPlayer.buy_card(card) # card.move(100, 0)
			return

	for token in Glob.tokens:
		if token.a[0]<=event.x<=token.b[0] and token.a[1]<=event.y<=token.b[1]:
			Glob.game.actualPlayer.get_token(token)
			return

# ~~heheszkiniewazne~~game.change_player()
### glowny program

Glob.root.title("Splendor")
Glob.canvas.pack()
Glob.canvas.bind("<Double-Button-1>", doubleB1)

for i in range(40):
	FirstLevelCard(50,350)

Glob.canvas.create_rectangle(50, 350, 50+Glob.SIZE_X, 350+Glob.SIZE_Y, fill='black')

for i in range(30):
	SecondLevelCard(50,200)

Glob.canvas.create_rectangle(50, 200, 50+Glob.SIZE_X, 200+Glob.SIZE_Y, fill='black')

for i in range(20):
	ThirdLevelCard(50,50)

Glob.canvas.create_rectangle(50, 50, 50+Glob.SIZE_X, 50+Glob.SIZE_Y, fill='black')

# TODO: te trzy prostkaty to karty majace zakrywać stosy. trzeba zrobić grafiki i wstawić

x=50
y=500
tmpStones = Glob.stonesNames*5
for i in tmpStones:
	if tmpStones.index(i)==0:
		x=50
		y+=10
	Token(x, y, i)
	x+=70
	


# TODO: zrobic z tego zmienna globalna bo może sie przydać w innych klasach
Glob.game = Game()
Glob.game.deal_cards()


Glob.root.mainloop()