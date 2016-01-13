# -*- coding: utf-8 -*-

from Globals import Glob
from Player import *
from Card import *

import tkMessageBox

class Game(object):
	def __init__(self):
		self.firstLev = [Glob.firstLevCards.pop() for i in range(4)]
		self.secLev = [Glob.secLevCards.pop() for i in range(4)]
		self.thirdLev = [Glob.thirdLevCards.pop() for i in range(4)]

		self.players = [Player(), Player()]
		self.actualPlayer = self.players[0]
		self.textId = Glob.canvas.create_text(Glob.WINDOW_X-5, 15, anchor='e', text='Player #'+str(self.actualPlayer.id))
		self.playerIter = self.player_iterator(0)
		self.nextTurn = self.make_button()

	def __getitem__(self):
		return self.firstLev + self.secLev + self.thirdLev

	# tworzenie przycisku do kończenia tury
	def make_button(self):
			b = Button(Glob.root, text='End Turn', command=self.change_player, state='disabled')
			b.pack()
			b.place(x=500, y=650)
			return b

	# rozkładane są 4 karty z każdego stosu - przygotowanie gry
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

	# gdy któraś z kart zostanie kupiona jest zastępowana odpowiednią ze stosu
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

	# zwracanie żetonu do puli
	def return_token(self, token):
		try:
			token.move(Glob.tokens[self.get_index(token.bonus)].a[0] - token.a[0], \
				Glob.tokens[self.get_index(token.bonus)].a[1] - token.a[1] + 10)
		except TypeError:
			token.move(Glob.tokensPos[token.bonus][0] - token.a[0], Glob.tokensPos[token.bonus][1] - token.a[1] + 10)

	# pobranie indeksu żetonu z puli, aby wiedzieć gdzie odłozyć żeton
	@staticmethod
	def get_index(stone):
		for token in Glob.tokens:
			if token.bonus==stone:
				return Glob.tokens.index(token)

	# sprawdza czy koniec rozgrywki
	def is_end(self):
		if(self.actualPlayer.state.vp>=15):
			tkMessageBox.showinfo("Koniec!", "Wygrał gracz #"+str(self.actualPlayer.id)+"!")
			Glob.canvas.unbind("<Button-1>")
			return True
		else:
			return False

	# funkcja zmiany gracza
	def change_player(self):
		Glob.game.nextTurn.config(state='disabled')
		
		for token in self.actualPlayer.tokens:
			Glob.canvas.itemconfig(token.tag, state='hidden')
		for card in self.actualPlayer.cards:
			Glob.canvas.itemconfig(card.tag, state='hidden')

		self.actualPlayer.tokenCount = 0
		self.actualPlayer.gotToken = False
		self.actualPlayer.tmpTokens = copy.deepcopy(Glob.stones)

		self.actualPlayer = self.playerIter.next()

		for token in self.actualPlayer.tokens:
			Glob.canvas.itemconfig(token.tag, state='normal')
		for card in self.actualPlayer.cards:
			Glob.canvas.itemconfig(card.tag, state='normal')

		Glob.canvas.delete(self.textId)
		self.textId = Glob.canvas.create_text(Glob.WINDOW_X-5, 15, anchor='e', text='Player #'+str(self.actualPlayer.id))

		self.actualPlayer.state.update_state()

	# funkcja iterująca po graczach w tablicy self.players
	def player_iterator(self, start):
		idx = start
		while True:
			idx += 1
			idx = idx % len(self.players)
			yield self.players[idx]