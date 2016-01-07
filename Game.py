# -*- coding: utf-8 -*-

from Globals import Glob
from Player import *
from Card import *


class Game(object):
	def __init__(self):
		self.firstLev = []
		self.secLev = []
		self.thirdLev = []
		for i in range(4):
			self.firstLev.append(Glob.firstLevCards.pop())
			self.secLev.append(Glob.secLevCards.pop())
			self.thirdLev.append(Glob.thirdLevCards.pop())

		self.players = [Player(), Player()]
		self.actualPlayer = self.players[0]
		self.textId = Glob.canvas.create_text(Glob.WINDOW_X-5, 5, anchor='e', text='Player #'+str(self.actualPlayer.id))

	def __getitem__(self):
		return self.firstLev + self.secLev + self.thirdLev

	def deal_cards(self):
		x = 170
		y1 = 350
		y2 = 200
		y3 = 50
		for i in range(4):
			tmp = self.firstLev[i]
			Glob.canvas.move(tmp.tag, x-tmp.a[0], y1-tmp.a[1])
			tmp.__setitem__(x, y1)

			tmp = self.secLev[i]
			Glob.canvas.move(tmp.tag, x-tmp.a[0], y2-tmp.a[1])
			tmp.__setitem__(x, y2)

			tmp = self.thirdLev[i]
			Glob.canvas.move(tmp.tag, x-tmp.a[0], y3-tmp.a[1])
			tmp.__setitem__(x, y3)

			x+=100

	def draw_new_card(self, cardLevel, card):
		if cardLevel==FirstLevelCard:
			self.firstLev.pop(self.firstLev.index(card))
			tmp = Glob.firstLevCards.pop()
			tmp.move(card.a[0]-tmp.a[0], card.a[1]-tmp.a[1])
			self.firstLev.insert(0, tmp)

		elif cardLevel==SecondLevelCard:
			self.secLev.pop(self.secLev.index(card))
			tmp = Glob.secLevCards.pop()
			tmp.move(card.a[0]-tmp.a[0], card.a[1]-tmp.a[1])
			self.secLev.insert(0, tmp)

		elif cardLevel==ThirdLevelCard:
			self.thirdLev.pop(self.thirdLev.index(card))
			tmp = Glob.thirdLevCards.pop()
			tmp.move(card.a[0]-tmp.a[0], card.a[1]-tmp.a[1])
			self.thirdLev.insert(0, tmp)

	def return_token(self, token):
		try:
			token.move(Glob.tokens[self.get_index(token.bonus)].a[0] - token.a[0], \
				Glob.tokens[self.get_index(token.bonus)].a[1] - token.a[1] + 10)
		except TypeError:
			token.move(Glob.tokensPos[token.bonus][0] - token.a[0], Glob.tokensPos[token.bonus][1] - token.a[1] + 10)

	@staticmethod
	def get_index(stone):
		for token in Glob.tokens:
			if token.bonus==stone:
				return Glob.tokens.index(token)

	# TODO: zmiana gracz. to juz wtedy gdy zrobie całą reszte
	def change_player(self):
		self.actualPlayer = self.players[1] if self.actualPlayer==self.players[0] else self.players[0]
		Glob.canvas.delete(self.textId)
		self.textId = Glob.canvas.create_text(Glob.WINDOW_X-5, 5, anchor='e', text='Player #'+str(self.actualPlayer.id))
			