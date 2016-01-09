# -*- coding: utf-8 -*-

from Globals import Glob
from Player import *
from Card import *


class Game(object):
	def __init__(self):
		self.firstLev = []  # zmien na list comprehension
		self.secLev = [] # tak samo
		self.thirdLev = [] # tak samo
		for i in range(4):
			self.firstLev.append(Glob.firstLevCards.pop())
			self.secLev.append(Glob.secLevCards.pop())
			self.thirdLev.append(Glob.thirdLevCards.pop())

		self.players = [Player(), Player()]
		self.actualPlayer = self.players[0]
		self.textId = Glob.canvas.create_text(Glob.WINDOW_X-5, 15, anchor='e', text='Player #'+str(self.actualPlayer.id))

	def __getitem__(self):
		return self.firstLev + self.secLev + self.thirdLev

	def deal_cards(self):
		x = 150
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

			x+=90

	def draw_new_card(self, cardLevel, card):
		if cardLevel==FirstLevelCard:
			self.firstLev.pop(self.firstLev.index(card))
			try:
				tmp = Glob.firstLevCards.pop()
				tmp.move(card.a[0]-tmp.a[0], card.a[1]-tmp.a[1])
				self.firstLev.insert(0, tmp)
			except IndexError:
				return

		elif cardLevel==SecondLevelCard:
			self.secLev.pop(self.secLev.index(card))
			try:
				tmp = Glob.secLevCards.pop()
				tmp.move(card.a[0]-tmp.a[0], card.a[1]-tmp.a[1])
				self.secLev.insert(0, tmp)
			except IndexError:
				return

		elif cardLevel==ThirdLevelCard:
			self.thirdLev.pop(self.thirdLev.index(card))
			try:
				tmp = Glob.thirdLevCards.pop()
				tmp.move(card.a[0]-tmp.a[0], card.a[1]-tmp.a[1])
				self.thirdLev.insert(0, tmp)
			except IndexError:
				return

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

	def is_end(self):
		if(self.actualPlayer.state.vp>=15):
			print "KONIEC! Wygrał gracz #" + str(self.actualPlayer.id)
			Glob.canvas.unbind("<Button-1>")
		# TODO: komunikat, pop up box, że kuniec

	def change_player(self):
		# TODO: dodaj ze trzeba wcisnac spacje żeby zmienić gracza

		for token in self.actualPlayer.tokens:
			Glob.canvas.itemconfig(token.tag, state='hidden')
		for card in self.actualPlayer.cards:
			Glob.canvas.itemconfig(card.tag, state='hidden')

		# self.actualPlayer.tokenCount = 0
		# self.actualPlayer.gotToken = False
		# self.actualPlayer.tmpTokens = copy.deepcopy(Glob.stones)
		# print self.actualPlayer.tokenCount
		# print self.actualPlayer.gotToken
		# print self.actualPlayer.tmpTokens
		self.actualPlayer.tokenCount = 0
		self.actualPlayer.gotToken = False
		self.actualPlayer.tmpTokens = copy.deepcopy(Glob.stones)

		self.actualPlayer = self.players[1] if self.actualPlayer==self.players[0] else self.players[0]

		# print self.actualPlayer.tokenCount
		# print self.actualPlayer.gotToken
		# print self.actualPlayer.tmpTokens

		for token in self.actualPlayer.tokens:
			Glob.canvas.itemconfig(token.tag, state='normal')
		for card in self.actualPlayer.cards:
			Glob.canvas.itemconfig(card.tag, state='normal')

		Glob.canvas.delete(self.textId)
		self.textId = Glob.canvas.create_text(Glob.WINDOW_X-5, 5, anchor='e', text='Player #'+str(self.actualPlayer.id))

		self.actualPlayer.state.update_state()
			